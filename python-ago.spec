#
# Conditional build:
%bcond_without	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module
#
%define	module	ago
#
Summary:	Makes customizable human readable timedeltas
Name:		python-ago
Version:	0.0.6
Release:	5
License:	public domain
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/a/ago/ago-%{version}.tar.gz
# Source0-md5:	e2fdc21fb922b4fc21ec19c6eac6bd46
Patch0:		ago-python3.patch
URL:		https://bitbucket.org/russellballestrini/ago/overview
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
Requires:	python
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Makes customizable human readable timedeltas.

%package -n	python3-%{module}
Summary:	Makes customizable human readable timedeltas
Group:		Libraries/Python
Requires:	python3

%description -n python3-%{module}
Makes customizable human readable timedeltas.

%prep
%setup  -q -n ago-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build --build-base py2
%endif
%if %{with python3}
%{__python3} %py_build --build-base py3
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
%py_build \
	--build-base py2 \
	install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%{__python3} %py_build \
	--build-base py3 \
	install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
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
