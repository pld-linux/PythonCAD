%include	/usr/lib/rpm/macros.python
Summary:	An open-source CAD package built designed around Python
Summary(pl):	Wolnodostêpny pakiet CAD oparty o Pythona
Name:		PythonCAD
Version:	DS1_R5
%define	_ver	%(echo %{version} | tr _ -)
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	http://www.pythoncad.org/releases/%{name}-%{_ver}.tar.bz2
URL:		http://www.pythoncad.org/
BuildRequires:	python
Requires:	python-pygtk-gtk >= 1.99.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PythonCAD is an open-source CAD package built designed around Python.
As such, it aims to be a fully scriptable and customizable CAD
program. It is initially designed to run under Linux, one of the BSD
flavors, or Unix.

%description -l pl
PythonCAD jest wolnodostêpnym pakietem CAD zbudowanym w oparciu o
Pythona. Dlatego ma byæ w pe³ni skryptowalnym i konfigurowalnym
programem CAD. Pocz±tkowo jest przeznaczony do uruchamiania pod
Linuksem, jedn± z wersji BSD lub Uniksem.

%prep
%setup -q -n %{name}-%{_ver}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install gtkpycad.py $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README PKG-INFO NEWS
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/%{name}*
