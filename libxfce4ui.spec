#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Various GTK+ widgets for Xfce
Summary(pl.UTF-8):	Różne widgety GTK+ dla Xfce
Name:		libxfce4ui
Version:	4.8.0
Release:	3
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://archive.xfce.org/xfce/4.8/src/libxfce4ui-%{version}.tar.bz2
# Source0-md5:	df9acb3328dff905bd0777b84532b69f
URL:		http://www.xfce.org/projects/libxfce4
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtk-doc
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool
BuildRequires:	libgladeui-devel >= 3.0.0
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xfce4-dev-tools >= 4.8.0
BuildRequires:	xfconf-devel >= %{version}
BuildRequires:	xorg-lib-libSM-devel
Requires:	xfconf >= %{version}
Obsoletes:	libxfcegui4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various GTK+ widgets for Xfce.

%description -l pl.UTF-8
Różne widgety GTK+ dla Xfce.

%package apidocs
Summary:	libxfce4ui API documentation
Summary(pl.UTF-8):	Dokumentacja API libxfce4ui
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	libxfcegui4-apidocs

%description apidocs
libxfce4ui API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libxfce4ui.

%package devel
Summary:	Development files for libxfce4ui library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxfc4ui
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.14.0
Requires:	libxfce4util-devel >= %{version}
Requires:	startup-notification-devel >= 0.8
Requires:	xfconf-devel >= %{version}
Requires:	xorg-lib-libSM-devel
Obsoletes:	libxfcegui4-devel

%description devel
Development files for the libxfce4ui library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libxfce4ui.

%package static
Summary:	Static libxfce4ui library
Summary(pl.UTF-8):	Statyczna biblioteka libxfce4ui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libxfcegui4-static

%description static
Static libxfce4ui library.

%description static -l pl.UTF-8
Statyczna biblioteka libxfce4ui.

%package -n glade3-libxfce4ui
Summary:	libxfce4ui support for Glade 3
Summary(pl.UTF-8):	Wsparcie dla libxfce4ui w Glade 3
Group:		Development/Building
Requires:	glade3

%description -n glade3-libxfce4ui
libxfce4ui support for Glade 3.

%description -n glade3-libxfce4ui -l pl.UTF-8
Wsparcie dla libxfce4ui w Glade 3.

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

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{tl_PH,ur_PK}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

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

%files -n glade3-libxfce4ui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/glade3/modules/libxfce4uiglade.so
%{_datadir}/glade3/catalogs/libxfce4ui.xml
%{_datadir}/glade3/catalogs/libxfce4ui.xml.in
%{_datadir}/glade3/pixmaps/*/*/*/*.png
