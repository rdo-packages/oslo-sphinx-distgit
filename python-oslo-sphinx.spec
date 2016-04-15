%global sname oslosphinx
%global pypi_name oslo-sphinx

%if 0%{?fedora}
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:       python-oslo-sphinx
Version:    4.3.0
Release:    1%{?dist}
Summary:    OpenStack Sphinx Extensions

License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    http://tarballs.openstack.org/%{sname}/%{sname}-%{version}.tar.gz
BuildArch:  noarch

%package -n python2-%{pypi_name}
Summary:    OpenStack Sphinx Extensions
%{?python_provide:%python_provide python2-%{pypi_name}}
%if 0%{?fedora} < 23
Obsoletes:  python-%{pypi_name} < %{version}-%{release}
%endif

Requires:   python-setuptools

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-d2to1
BuildRequires: python-pbr

Requires:      git
Requires:      python-requests >= 2.5.2
Requires:      python-pbr
Requires:      python-six >= 1.9.0

# tests
BuildRequires: python-requests >= 2.5.2

%description -n python2-%{pypi_name}
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-sphinx library contains Sphinx theme and extensions support used by
OpenStack.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:    OpenStack Sphinx Extensions
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:   python3-setuptools

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-d2to1
BuildRequires: python3-pbr

Requires:      python3-requests >= 2.5.2
Requires:      python3-pbr
Requires:      python3-six >= 1.9.0

# tests
BuildRequires: python3-requests >= 2.5.2

%description -n python3-%{pypi_name}
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-sphinx library contains Sphinx theme and extensions support used by
OpenStack.
%endif

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-sphinx library contains Sphinx theme and extensions support used by
OpenStack.

%prep
%setup -q -n oslosphinx-%{upstream_version}
# Remove bundled egg-info
rm -rf oslo_sphinx.egg-info
rm -rf {test-,}requirements.txt

%build
%{__python2} setup.py build
%if 0%{?with_python3}
%{__python3} setup.py build
%endif

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%if 0%{?with_python3}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
%endif

%check
%{__python2} setup.py test
%if 0%{?with_python3}
%{__python3} setup.py test
%endif

## Fix hidden-file-or-dir warnings
#rm -fr doc/build/html/.buildinfo

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslosphinx
%{python2_sitelib}/oslosphinx*.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslosphinx
%{python3_sitelib}/oslosphinx*.egg-info
%endif


%changelog
* Mon Mar 21 2016 Haikel Guemar <hguemar@fedoraproject.org> 4.3.0-
- Update to 4.3.0

