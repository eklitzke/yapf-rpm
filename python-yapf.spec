# Created by pyp2rpm-3.3.2
%global pypi_name yapf

Name:           python-%{pypi_name}
Version:        0.22.0
Release:        1%{?dist}
Summary:        A formatter for Python code

License:        ASL 2.0
URL:            https://github.com/google/yapf
Source0:        https://files.pythonhosted.org/packages/source/y/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
YAPF is Yet Another Python Formatter. It automatically reformats source files to
conform to conform to PEP 8 and other Python coding best practices.

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2dist(setuptools)
%description -n python2-%{pypi_name}
YAPF is Yet Another Python Formatter. It automatically reformats source files to
conform to conform to PEP 8 and other Python coding best practices.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
YAPF is Yet Another Python Formatter. It automatically reformats source files to
conform to conform to PEP 8 and other Python coding best practices.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
rm -rf %{buildroot}%{_bindir}/*
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/yapftests
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/yapf
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/yapftests
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun May 20 2018 Dick Marinus <dick@mrns.nl> - 0.22.0-1
- v0.22.0

* Sun May 20 2018 Dick Marinus <dick@mrns.nl> - 0.21.0-5
- Fix url tag

* Sun May 20 2018 Dick Marinus <dick@mrns.nl> - 0.21.0-4
- Fix license tag

* Tue May 15 2018 Evan Klitzke <evan@eklitzke.org> - 0.21.0-3
- Convert package to pyp2rpm format.

* Thu May 10 2018 Evan Klitzke <evan@eklitzke.org> - 0.21.0-2
- Update packaging to handle py2/py3 better

* Sat Apr 21 2018 Evan Klitzke <evan@eklitzke.org> - 0.21.0-1
- Initial packaging work.
