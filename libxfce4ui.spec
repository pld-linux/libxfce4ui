#
# Conditional build:
%bcond_without	gladeui2	# Glade catalog
%bcond_with	static_libs	# static library

%define		xfce_version	4.18.0
Summary:	Various GTK+ widgets for Xfce
Summary(pl.UTF-8):	Różne widgety GTK+ dla Xfce
Name:		libxfce4ui
Version:	4.18.3
Release:	1
License:	LGPL v2
Group:		X11/Libraries
Source0:	https://archive.xfce.org/src/xfce/libxfce4ui/4.18/%{name}-%{version}.tar.bz2
# Source0-md5:	740cecafa50b733f39d56c9fbb74c68e
Patch0:		%{name}-link.patch
URL:		https://www.xfce.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
%{?with_gladeui2:BuildRequires:	glade-devel >= 3.5.0}
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gobject-introspection-devel >= 1.66.0
BuildRequires:	gtk+3-devel >= 3.18.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gtk-doc-automake >= 1.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgtop-devel >= 2.24.0
BuildRequires:	libgudev-devel >= 232
BuildRequires:	libtool >= 2:2.4
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 2.000
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	vala
BuildRequires:	vala-libxfce4util >= 4.18.0
BuildRequires:	xfce4-dev-tools >= 4.18.0
BuildRequires:	xfconf-devel >= %{xfce_version}
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	%{name}-about
Requires:	glib2 >= 1:2.50.0
Requires:	gtk+3 >= 3.18.0
Requires:	libxfce4util >= %{xfce_version}
Requires:	startup-notification >= 0.8
Requires:	xfconf >= %{xfce_version}
Obsoletes:	xfce4-quicklauncher-plugin < 1.10
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
Requires:	glib2-devel >= 1:2.50.0
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
BuildArch:	noarch

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
BuildArch:	noarch

%description -n vala-libxfce4ui
Vala API for libxfce4ui library.

%description -n vala-libxfce4ui -l pl.UTF-8
API języka Vala do biblioteki libxfce4ui.

%package -n glade-libxfce4ui
Summary:	libxfce4ui support for Glade
Summary(pl.UTF-8):	Wsparcie dla libxfce4ui w Glade
Group:		Development/Building
Requires:	%{name} = %{version}-%{release}
Requires:	glade-libs >= 3.5.0
Obsoletes:	glade3-libxfce4ui < 4.16

%description -n glade-libxfce4ui
libxfce4ui support for Glade.

%description -n glade-libxfce4ui -l pl.UTF-8
Wsparcie dla libxfce4ui w Glade.

%prep
%setup -q
%patch0 -p1

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
	%{__enable_disable gladeui2} \
	--with-html-dir=%{_gtkdocdir} \
	--with-vendor-info="PLD Linux"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with gladeui2}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/glade/modules/libxfce4uiglade2.la
%{?with_static_libs:%{__rm} $RPM_BUILD_ROOT%{_libdir}/glade/modules/libxfce4uiglade2.a}
%endif

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
# duplicates of hy,ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hy_AM,ur_PK}
# not supported by glibc (as of 2.32)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libxfce4kbd-private-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4kbd-private-3.so.0
%attr(755,root,root) %{_libdir}/libxfce4ui-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4ui-2.so.0
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
%{_libdir}/girepository-1.0/Libxfce4ui-2.0.typelib

%files about
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xfce4-about
%{_desktopdir}/xfce4-about.desktop
%{_iconsdir}/hicolor/*x*/apps/xfce4-logo.png
%{_iconsdir}/hicolor/*x*/apps/org.xfce.about.png
%{_iconsdir}/hicolor/scalable/apps/xfce4-logo.svg
%{_iconsdir}/hicolor/scalable/apps/org.xfce.about.svg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4kbd-private-3.so
%attr(755,root,root) %{_libdir}/libxfce4ui-2.so
%{_includedir}/xfce4/libxfce4kbd-private-3
%{_includedir}/xfce4/libxfce4ui-2
%{_pkgconfigdir}/libxfce4kbd-private-3.pc
%{_pkgconfigdir}/libxfce4ui-2.pc
%{_datadir}/gir-1.0/Libxfce4ui-2.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxfce4kbd-private-3.a
%{_libdir}/libxfce4ui-2.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files -n vala-libxfce4ui
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libxfce4ui-2.deps
%{_datadir}/vala/vapi/libxfce4ui-2.vapi

%if %{with gladeui2}
%files -n glade-libxfce4ui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/glade/modules/libxfce4uiglade2.so
%{_datadir}/glade/catalogs/libxfce4ui-2.xml
%{_datadir}/glade/pixmaps/hicolor/*x*/actions/widget-libxfce4ui-xfce-titled-dialog.png
%endif
