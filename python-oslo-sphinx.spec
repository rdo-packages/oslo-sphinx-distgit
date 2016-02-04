%global pypi_name oslosphinx

%if 0%{?fedora}
%global with_python3 1
%endif

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:       python-oslo-sphinx
Version:    3.1.0
Release:    3%{?dist}
Summary:    OpenStack Sphinx Extensions and Theme for Python 2

License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:  noarch
Requires:   python-setuptools

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-pbr

%description
The Oslo project intends to produce a python 2 library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-sphinx library contains Sphinx theme and extensions support used by
OpenStack.

%if 0%{?with_python3}
%package -n python3-oslo-sphinx
Summary:        OpenStack Sphinx Extensions and Theme for Python 3
License:        ASL 2.0
BuildArch:  noarch
Requires:   python3-setuptools

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr
%endif

%if 0%{?with_python3}
%description -n python3-oslo-sphinx
The Oslo project intends to produce a python 3 library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-sphinx library contains Sphinx theme and extensions support used by
OpenStack.
%endif

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if 0%{?with_python3}
cp -a . %{py3dir}
%endif

%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif


%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

# create backward compatibile oslo.sphinx namespace package
mkdir oslo
mv oslosphinx oslo/sphinx
sed -i 's/oslosphinx/oslo.sphinx/' oslo/sphinx/intersphinx.py
sed -i '/packages =/ { N; s/oslosphinx/oslo\n\toslo.sphinx\nnamespace_packages =\n\toslo/ }' setup.cfg
%{__python2} setup.py build
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
ln -s ../../oslosphinx/theme %{buildroot}%{python2_sitelib}/oslo/sphinx

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
popd
%endif

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/oslo
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/*-nspkg.pth

%if 0%{?with_python3}
%files -n python3-oslo-sphinx
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/*.egg-info
%endif

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Aug 16 2015 Alan Pevec <alan.pevec@redhat.com> 3.1.0-1
- Update to upstream 3.1.0

* Thu Jun 25 2015 Alan Pevec <alan.pevec@redhat.com> 3.0.0-1
- Update to upstream 3.0.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Alan Pevec <alan.pevec@redhat.com> - 2.5.0-1
- Update to 2.5.0

* Fri Mar 13 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.3.0-3
- Added python3 subpackage

* Mon Dec 15 2014 Alan Pevec <alan.pevec@redhat.com> - 2.3.0-2
- Update to 2.3.0
- Provide oslo.sphinx theme compatibility symlink

* Tue Nov 04 2014 Alan Pevec <alan.pevec@redhat.com> - 2.2.0-1
- Update to 2.2.0
- Provide both old oslo.sphinx namespaced package and new oslosphinx

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 07 2014 Pádraig Brady <pbrady@redhat.com> - 1.1-1
- Update to release 1.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Pádraig Brady <pbrady@redhat.com> 1.0-3
- Review adjustments

* Mon Jul 8 2013 Dan Prince <dprince@redhat.com> 1.0-1
- Initial package.
