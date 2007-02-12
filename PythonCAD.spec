%define	_ver	%(echo %{version} | tr _ -)
Summary:	An open-source CAD package built designed around Python
Summary(pl.UTF-8):	Wolnodostępny pakiet CAD oparty o Pythona
Name:		PythonCAD
Version:	DS1_R28
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	http://www.pythoncad.org/releases/%{name}-%{_ver}.tar.bz2
# Source0-md5:	2c310626518b875d998ce2fd391d79bb
URL:		http://www.pythoncad.org/
BuildRequires:	python-devel >= 2.3
%pyrequires_eq	python-libs
Requires:	python-pygtk-gtk >= 2.6.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PythonCAD is an open-source CAD package built designed around Python.
As such, it aims to be a fully scriptable and customizable CAD
program. It is initially designed to run under Linux, one of the BSD
flavors, or Unix.

%description -l pl.UTF-8
PythonCAD jest wolnodostępnym pakietem CAD zbudowanym w oparciu
o Pythona. Dlatego ma być w pełni skryptowalnym i konfigurowalnym
programem CAD. Jest przeznaczony do uruchamiania pod Linuksem, jedną
z wersji BSD lub Uniksem.

%prep
%setup -q -n %{name}-%{_ver}

cat <<'EOF' >PythonCad.sh
#!/bin/sh
exec python %{py_sitescriptdir}/%{name}/gtkpycad.py $@
EOF

sed -i -e 's#Exec=/usr/bin/gtkpycad.py#Exec=PythonCad#' pythoncad.desktop
sed -i -e 's#Categories=Office;Graphics;Application;Utility;X-Red-Hat-Base;#Categories=Utility;Engineering;#' pythoncad.desktop
echo 'Comment[pl]=Aplikacja typ CAD' >> pythoncad.desktop
echo '# vi: encoding=utf-8' >> pythoncad.desktop

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_desktopdir},%{_pixmapsdir},%{py_sitescriptdir}/%{name}}
install -Dp PythonCad.sh $RPM_BUILD_ROOT%{_bindir}/PythonCad
cp pythoncad.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp prefs.py $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
cp gtkpycad.png $RPM_BUILD_ROOT%{_pixmapsdir}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" | xargs rm
cp gtkpycad.py $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README PKG-INFO NEWS
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
%{_sysconfdir}/%{name}
%{_desktopdir}/pythoncad.desktop
%{_pixmapsdir}/*.png
