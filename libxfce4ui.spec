#
# Conditional build:
%bcond_without	glade3		# Glade3 catalog
%bcond_with	static_libs	# static library

%define		xfce_version	4.13.1
Summary:	Various GTK+ widgets for Xfce
Summary(pl.UTF-8):	Różne widgety GTK+ dla Xfce
Name:		libxfce4ui
Version:	4.13.6
Release:	2
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://archive.xfce.org/src/xfce/libxfce4ui/4.13/%{name}-%{version}.tar.bz2
# Source0-md5:	9e5a805d2d557df79e571468978a2766
URL:		https://www.xfce.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
# if no glade3, then glade 3.x catalog can be installed
#BuildRequires:	glade-devel >= 3.5.0
BuildRequires:	glib2-devel >= 1:2.42.0
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk+2-devel >= 2:2.24.0
BuildRequires:	gtk+3-devel >= 3.18.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gtk-doc-automake >= 1.0
BuildRequires:	intltool >= 0.35.0
%{?with_glade3:BuildRequires:	libgladeui-devel >= 3.5.0}
BuildRequires:	libtool >= 2:2.4
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	vala
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	xfconf-devel >= %{xfce_version}
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	%{name}-about
Requires:	glib2 >= 1:2.42.0
Requires:	gtk+2 >= 2:2.24.0
Requires:	gtk+3 >= 3.18.0
Requires:	libxfce4util >= %{xfce_version}
Requires:	startup-notification >= 0.8
Requires:	xfconf >= %{xfce_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various GTK+ widgets for Xfce.

%description -l pl.UTF-8
Różne widgety GTK+ dla Xfce.

%package about
Summary:	Information about the Xfce Desktop Environment
Summary(pl.UTF-8):	Informacje o środowisku graficznym Xfce
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description about
Information about the Xfce Desktop Environment.

%description about -l pl.UTF-8
Informacje o środowisku graficznym Xfce.

%package devel
Summary:	Development files for libxfce4ui library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxfce4ui
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.42.0
Requires:	gtk+2-devel >= 2:2.24.0
Requires:	gtk+3-devel >= 3.18.0
Requires:	libxfce4util-devel >= %{xfce_version}
Requires:	startup-notification-devel >= 0.8
Requires:	xfconf-devel >= %{xfce_version}
Requires:	xorg-lib-libSM-devel

%description devel
Development files for the libxfce4ui library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libxfce4ui.

%package static
Summary:	Static libxfce4ui library
Summary(pl.UTF-8):	Statyczna biblioteka libxfce4ui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxfce4ui library.

%description static -l pl.UTF-8
Statyczna biblioteka libxfce4ui.

%package apidocs
Summary:	libxfce4ui API documentation
Summary(pl.UTF-8):	Dokumentacja API libxfce4ui
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
libxfce4ui API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libxfce4ui.

%package -n vala-libxfce4ui
Summary:	Vala API for libxfce4ui library
Summary(pl.UTF-8):	API języka Vala do biblioteki libxfce4ui
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala-libxfce4util
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-libxfce4ui
Vala API for libxfce4ui library.

%description -n vala-libxfce4ui -l pl.UTF-8
API języka Vala do biblioteki libxfce4ui.

%package -n glade3-libxfce4ui
Summary:	libxfce4ui support for Glade 3
Summary(pl.UTF-8):	Wsparcie dla libxfce4ui w Glade 3
Group:		Development/Building
Requires:	%{name} = %{version}-%{release}
Requires:	glade3 >= 3.5.0

%description -n glade3-libxfce4ui
libxfce4ui support for Glade 3.

%description -n glade3-libxfce4ui -l pl.UTF-8
Wsparcie dla libxfce4ui w Glade 3.

%prep
%setup -q

mkdir -p m4

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with glade3}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/glade3/modules/libxfce4uiglade.la
%{?with_static_libs:%{__rm} $RPM_BUILD_ROOT%{_libdir}/glade3/modules/libxfce4uiglade.a}
%endif

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
# unify
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}
# just a copy of ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK
# not supported by glibc (as of 2.29)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libxfce4kbd-private-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4kbd-private-2.so.0
%attr(755,root,root) %{_libdir}/libxfce4kbd-private-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4kbd-private-3.so.0
%attr(755,root,root) %{_libdir}/libxfce4ui-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4ui-1.so.0
%attr(755,root,root) %{_libdir}/libxfce4ui-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4ui-2.so.0
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
%{_libdir}/girepository-1.0/libxfce4ui-2.0.typelib

%files about
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xfce4-about
%{_desktopdir}/xfce4-about.desktop
%{_iconsdir}/hicolor/48x48/apps/xfce4-logo.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4kbd-private-2.so
%attr(755,root,root) %{_libdir}/libxfce4kbd-private-3.so
%attr(755,root,root) %{_libdir}/libxfce4ui-1.so
%attr(755,root,root) %{_libdir}/libxfce4ui-2.so
%{_includedir}/xfce4/libxfce4kbd-private-2
%{_includedir}/xfce4/libxfce4kbd-private-3
%{_includedir}/xfce4/libxfce4ui-1
%{_includedir}/xfce4/libxfce4ui-2
%{_pkgconfigdir}/libxfce4kbd-private-2.pc
%{_pkgconfigdir}/libxfce4kbd-private-3.pc
%{_pkgconfigdir}/libxfce4ui-1.pc
%{_pkgconfigdir}/libxfce4ui-2.pc
%{_datadir}/gir-1.0/libxfce4ui-2.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxfce4kbd-private-2.a
%{_libdir}/libxfce4ui-1.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files -n vala-libxfce4ui
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libxfce4ui-2.deps
%{_datadir}/vala/vapi/libxfce4ui-2.vapi

%if %{with glade3}
%files -n glade3-libxfce4ui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/glade3/modules/libxfce4uiglade.so
%{_datadir}/glade3/catalogs/libxfce4ui.xml
%{_datadir}/glade3/pixmaps/hicolor/*x*/actions/widget-libxfce4ui-xfce-titled-dialog.png
%endif
