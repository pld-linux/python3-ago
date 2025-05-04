%define	module	ago
#
Summary:	Makes customizable human readable timedeltas
Summary(pl.UTF-8):	Konfigurowalne, czytelne dla człowieka różnice czasu
Name:		python3-ago
Version:	0.1.0
Release:	1
License:	Public Domain
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ago/
Source0:	https://files.pythonhosted.org/packages/source/a/ago/ago-%{version}.tar.gz
# Source0-md5:	669635e6283b6aa9334184684ca2f062
URL:		https://bitbucket.org/russellballestrini/ago/overview
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Makes customizable human readable timedeltas.

%description -l pl.UTF-8
Konfigurowalne, czytelne dla człowieka różnice czasu.

%prep
%setup -q -n ago-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO README.rst
%{_examplesdir}/python3-%{module}-%{version}
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/*egg-info
