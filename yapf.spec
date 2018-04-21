%global srcname yapf
%global sum A code formatter for Python

Name:           python-%{srcname}
Version:        0.21.0
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/d0/68/7c0be88aa4cc7daf45294cc41c749dac02600933bf23e41d0d941d17d569/yapf-0.21.0.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python3-devel

%description
An automatic code formatting utility for Python.

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
An automatic code formatting utility for Python.


%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
An automatic code formatting utility for Python.


%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
# If, however, we're installing separate executables for python2 and python3,
# the order needs to be reversed so the unversioned executable is the python2 one.
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{srcname}
%doc README.rst
%{python2_sitelib}/*
%{_bindir}/yapf

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/*
%{_bindir}/yapf

%changelog
