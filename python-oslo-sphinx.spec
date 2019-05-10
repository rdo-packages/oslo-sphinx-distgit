%global sname oslosphinx
%global pypi_name oslo-sphinx

%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%endif

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
Version:    4.18.0
Release:    1%{?dist}
Summary:    OpenStack Sphinx Extensions

License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    https://tarballs.openstack.org/%{sname}/%{sname}-%{version}.tar.gz
BuildArch:  noarch

%package -n python2-%{pypi_name}
Summary:    OpenStack Sphinx Extensions
%{?python_provide:%python_provide python2-%{pypi_name}}
%if 0%{?fedora} < 23
Obsoletes:  python-%{pypi_name} < %{version}-%{release}
%endif

Requires:   python2-setuptools

BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-pbr
%if 0%{?fedora} > 0 || 0%{?rhel} > 7
BuildRequires: python2-d2to1
%else
BuildRequires: python-d2to1
%endif

Requires:      git
Requires:      python2-requests >= 2.14.2
Requires:      python2-pbr
Requires:      python2-six >= 1.10.0

# tests
BuildRequires: python2-requests >= 2.14.2

%description -n python2-%{pypi_name}
%{common_desc}

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:    OpenStack Sphinx Extensions
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:   python3-setuptools

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-d2to1
BuildRequires: python3-pbr

Requires:      python3-requests >= 2.14.2
Requires:      python3-pbr
Requires:      python3-six >= 1.10.0

# tests
BuildRequires: python3-requests >= 2.14.2

%description -n python3-%{pypi_name}
%{common_desc}
%endif

%description
%{common_desc}

%prep
%setup -q -n %{sname}-%{upstream_version}
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
%{python2_sitelib}/%{sname}
%{python2_sitelib}/%{sname}*.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{sname}*.egg-info
%endif


%changelog
* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 4.18.0-1
- Update to 4.18.0

