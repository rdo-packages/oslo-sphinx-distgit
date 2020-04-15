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

%package -n python3-%{pypi_name}
Summary:    OpenStack Sphinx Extensions
%{?python_provide:%python_provide python3-%{pypi_name}}


BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr
# tests
BuildRequires: python3-requests >= 2.14.2

Requires:      git
Requires:      python3-requests >= 2.14.2
Requires:      python3-pbr
Requires:      python3-six >= 1.10.0
Requires:      python3-setuptools


%description -n python3-%{pypi_name}
%{common_desc}

%description
%{common_desc}

%prep
%setup -q -n %{sname}-%{upstream_version}
# Remove bundled egg-info
rm -rf oslo_sphinx.egg-info
rm -rf {test-,}requirements.txt

%build
%{py3_build}

%install
%{py3_install}

%check
python3 setup.py test

## Fix hidden-file-or-dir warnings
#rm -fr doc/build/html/.buildinfo

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{sname}*.egg-info


%changelog
