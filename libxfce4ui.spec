#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Various GTK+ widgets for Xfce
Summary(pl.UTF-8):	Różne widgety GTK+ dla Xfce
Name:		libxfce4ui
Version:	4.7.4
Release:	0.1
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://www.xfce.org/archive/xfce/4.8pre1/src/%{name}-%{version}.tar.bz2
# Source0-md5:	4d3cc02c6b09552b940d5d09245e8934
URL:		http://www.xfce.org/projects/libraries/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	gtk-doc
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgladeui-devel >= 3.0.0
BuildRequires:	libtool
#BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	libxfce4util-devel >= 4.7.3
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xfce4-dev-tools >= 4.7.0
#BuildRequires:	xfconf-devel >= %{version}
BuildRequires:	xfconf-devel >= 4.7.3
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	xfconf >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various GTK+ widgets for Xfce.

%description -l pl.UTF-8
Różne widgety GTK+ dla Xfce.

%package apidocs
Summary:	libxfcegui4 API documentation
Summary(pl.UTF-8):	Dokumentacja API libxfcegui4
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libxfcegui4 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libxfcegui4.

%package devel
Summary:	Development files for libxfcegui4 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxfcegui4
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.6
#Requires:	libxfce4util-devel >= %{version}
Requires:	libxfce4util-devel >= %{version}
Requires:	startup-notification-devel >= 0.8
#Requires:	xfconf-devel >= %{version}
Requires:	xfconf-devel >= 4.7.3
Requires:	xorg-lib-libSM-devel

%description devel
Development files for the libxfcegui4 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libxfcegui4.

%package static
Summary:	Static libxfcegui4 library
Summary(pl.UTF-8):	Statyczna biblioteka libxfcegui4
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxfcegui4 library.

%description static -l pl.UTF-8
Statyczna biblioteka libxfcegui4.

%package -n glade3-libxfcegui4
Summary:	libxfcegui4 support for Glade 3
Summary(pl.UTF-8):	Wsparcie dla libxfcegui4 w Glade 3
Group:		Development/Building
Requires:	glade3

%description -n glade3-libxfcegui4
libxfcegui4 support for Glade 3.

%description -n glade3-libxfcegui4 -l pl.UTF-8
Wsparcie dla libxfcegui4 w Glade 3.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--%{?with_static_libs:en}%{!?with_static_libs:dis}able-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/glade3/modules/libxfce4uiglade.la
%{?with_static_libs:%{__rm} $RPM_BUILD_ROOT%{_libdir}/glade3/modules/libxfce4uiglade.a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libxfce4kbd-private-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4kbd-private-2.so.0
%attr(755,root,root) %{_libdir}/libxfce4ui-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4ui-1.so.0
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4kbd-private-2.so
%attr(755,root,root) %{_libdir}/libxfce4ui-1.so
%{_libdir}/libxfce4kbd-private-2.la
%{_libdir}/libxfce4ui-1.la
%{_includedir}/xfce4/libxfce4kbd-private-2
%{_includedir}/xfce4/libxfce4ui-1
%{_pkgconfigdir}/libxfce4kbd-private-2.pc
%{_pkgconfigdir}/libxfce4ui-1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxfce4kbd-private-2.a
%{_libdir}/libxfce4ui-1.a
%endif

%files -n glade3-libxfcegui4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/glade3/modules/libxfce4uiglade.so
%{_datadir}/glade3/catalogs/libxfce4ui.xml
%{_datadir}/glade3/catalogs/libxfce4ui.xml.in
%{_datadir}/glade3/pixmaps/*/*/*/*.png
