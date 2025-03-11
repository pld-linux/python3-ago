#
# Conditional build:
%bcond_without	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module
#
%define	module	ago
#
Summary:	Makes customizable human readable timedeltas
Summary(pl.UTF-8):	Konfigurowalne, czytelne dla człowieka różnice czasu
Name:		python-ago
Version:	0.0.6
Release:	17
License:	Public Domain
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ago/
Source0:	https://files.pythonhosted.org/packages/source/a/ago/ago-%{version}.tar.gz
# Source0-md5:	e2fdc21fb922b4fc21ec19c6eac6bd46
Patch0:		ago-python3.patch
URL:		https://bitbucket.org/russellballestrini/ago/overview
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Makes customizable human readable timedeltas.

%description -l pl.UTF-8
Konfigurowalne, czytelne dla człowieka różnice czasu.

%package -n python3-%{module}
Summary:	Makes customizable human readable timedeltas
Summary(pl.UTF-8):	Konfigurowalne, czytelne dla człowieka różnice czasu
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Makes customizable human readable timedeltas.

%description -n python3-%{module} -l pl.UTF-8
Konfigurowalne, czytelne dla człowieka różnice czasu.

%prep
%setup -q -n ago-%{version}
%patch -P 0 -p1

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
%py_install
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc PKG-INFO README.rst
%{_examplesdir}/python-%{module}-%{version}
%{py_sitescriptdir}/%{module}.py*
%{py_sitescriptdir}/*egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc PKG-INFO README.rst
%{_examplesdir}/python3-%{module}-%{version}
%{py3_sitescriptdir}/%{module}.py*
%{py3_sitescriptdir}/__pycache__/ago.cpython-*.py*
%{py3_sitescriptdir}/*egg-info
%endif
