%define		_enable_debug_packages	0

%define module	zope.deferredimport
Summary:	Defer Python module import
Summary(pl.UTF-8):	Opóźnianie importu modułów Pythona
Name:		python-%{module}
Version:	3.5.3
Release:	3
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/z/zope.deferredimport/zope.deferredimport-%{version}.tar.gz
# Source0-md5:	68fce3bf4f011d4a840902fd763884ee
URL:		http://www.zope.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
Requires:	python-zope.proxy
Requires:	python-zope.testing
Obsoletes:	Zope-DeferredImport
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Defer Python module import.

%description -l pl.UTF-8
Opóźnianie importu modułów Pythona.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--install-purelib=%{py_sitescriptdir} \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/zope/deferredimport
%{py_sitescriptdir}/zope.deferredimport-*.egg-info
%{py_sitescriptdir}/zope.deferredimport-*-nspkg.pth
