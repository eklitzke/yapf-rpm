%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without python3
%if 0%{?fedora} > 26 || 0%{?rhel} > 7
%global defaultpython 3
%else
%global defaultpython 2
%endif
%else
%bcond_with python3
%global defaultpython 2
%endif

%global modname yapf
%global sum  A formatter for Python files
%global desc An automatic code formatting utility for Python.

Name:           python-%{modname}
Version:        0.21.0
Release:        2%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{modname}
Source0:        https://files.pythonhosted.org/packages/d0/68/7c0be88aa4cc7daf45294cc41c749dac02600933bf23e41d0d941d17d569/yapf-0.21.0.tar.gz

BuildArch:      noarch

%description
YAPF is an automatic code formatting utility for Python.

%package -n python2-%{modname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{modname}}

Requires:       python2-setuptools

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description -n python2-%{modname}
%{desc}

%if %{with python3}
%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

Requires:       python3-setuptools

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python%{python3_pkgversion}-%{modname}
%{desc}
%endif

%prep
%autosetup -n %{modname}-%{version}

%build
%py2_build
%if %{with python3}
%py3_build
%endif

%install

%py2_install
mv %{buildroot}%{_bindir}/yapf %{buildroot}%{_bindir}/yapf-2
ln -s yapf-2 %{buildroot}%{_bindir}/yapf-%{python2_version}

%if %{with python3}
%py3_install
mv %{buildroot}%{_bindir}/yapf %{buildroot}%{_bindir}/yapf-3
ln -s yapf-3 %{buildroot}%{_bindir}/yapf-%{python3_version}
%endif

ln -s yapf-%{defaultpython} %{buildroot}%{_bindir}/yapf

%check
%{__python2} setup.py test
%{?with_python3:%{__python3} setup.py test}

%files -n python2-%{modname}
%doc README.rst
%if %{defaultpython} == 2
%{_bindir}/yapf
%endif
%{_bindir}/yapf-2
%{_bindir}/yapf-%{python2_version}
%{python2_sitelib}/*

%if %{with python3}
%files -n python%{python3_pkgversion}-%{modname}
%doc README.rst
%if %{defaultpython} == 3
%{_bindir}/yapf
%endif
%{_bindir}/yapf-3
%{_bindir}/yapf-%{python3_version}
%{python3_sitelib}/%{modname}*
%endif

%changelog
* Thu May 10 2018 Evan Klitzke <evan@eklitzke.org> - 0.21.0-2
- Update packaging to handle py2/py3 better

* Sat Apr 21 2018 Evan Klitzke <evan@eklitzke.org> - 0.21.0-1
- Initial packaging work.
