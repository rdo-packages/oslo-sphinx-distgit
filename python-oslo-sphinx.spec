# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%global sname oslosphinx
%global pypi_name oslo-sphinx

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
The Oslo project intends to produce a python library containing \
infrastructure code shared by OpenStack projects. The APIs provided \
by the project should be high quality, stable, consistent and generally \
useful. \
 \
The oslo-sphinx library contains Sphinx theme and extensions support used by \
OpenStack.

Name:       python-oslo-sphinx
Version:    XXX
Release:    XXX
Summary:    OpenStack Sphinx Extensions

License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    https://tarballs.openstack.org/%{sname}/%{sname}-%{version}.tar.gz
BuildArch:  noarch

%package -n python%{pyver}-%{pypi_name}
Summary:    OpenStack Sphinx Extensions
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}}


BuildRequires: python%{pyver}-devel
BuildRequires: python%{pyver}-setuptools
BuildRequires: python%{pyver}-pbr
# tests
BuildRequires: python%{pyver}-requests >= 2.14.2
# Handle python2 exception
%if %{pyver} == 2
BuildRequires: python-d2to1
%else
BuildRequires: python%{pyver}-d2to1
%endif

Requires:      git
Requires:      python%{pyver}-requests >= 2.14.2
Requires:      python%{pyver}-pbr
Requires:      python%{pyver}-six >= 1.10.0
Requires:      python%{pyver}-setuptools


%description -n python%{pyver}-%{pypi_name}
%{common_desc}

%description
%{common_desc}

%prep
%setup -q -n %{sname}-%{upstream_version}
# Remove bundled egg-info
rm -rf oslo_sphinx.egg-info
rm -rf {test-,}requirements.txt

%build
%{pyver_bin} setup.py build

%install
%{pyver_install}

%check
%{pyver_bin} setup.py test

## Fix hidden-file-or-dir warnings
#rm -fr doc/build/html/.buildinfo

%files -n python%{pyver}-%{pypi_name}
%license LICENSE
%doc README.rst
%{pyver_sitelib}/%{sname}
%{pyver_sitelib}/%{sname}*.egg-info


%changelog
