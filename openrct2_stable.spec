#%if 0%{?fedora} >= 35
#%_cmake_flag -Wno-deprecated-declarations
#%endif

Name: 		openrct2
Version: 	0.3.5.1
Release: 	1%{?dist}
Summary: 	Open source reimplementation of Roller Coaster Tycoon 2

License: 	GPLv3
URL: 		https://www.openrct2.io
Source0:	https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc gcc-c++ json-devel pkgconfig openssl-devel SDL2-devel speexdsp-devel libcurl-devel cmake libicu-devel fontconfig-devel freetype-devel libpng-devel libzip-devel mesa-libGL-devel duktape-devel qgis-devel ninja-build

%description
OpenRCT2 is a free open source remake of the famous RollerCoaster Tycoon 2 game.

%prep
%setup -q -n OpenRCT2-%{version}

%build
mkdir build
cd build
%cmake -G Ninja -DDISABLE_GOOGLE_BENCHMARK:BOOL=ON -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BINARY_DIR=usr ..
ln -s ../data data
%install
cd build
%cmake_install

%files
%{_bindir}/*
%{_libdir}/*

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*

%{_datadir}/metainfo/*

%{_datadir}/icons/hicolor/16x16/apps/openrct2.png
%{_datadir}/icons/hicolor/24x24/apps/openrct2.png
%{_datadir}/icons/hicolor/32x32/apps/openrct2.png
%{_datadir}/icons/hicolor/48x48/apps/openrct2.png
%{_datadir}/icons/hicolor/64x64/apps/openrct2.png
%{_datadir}/icons/hicolor/96x96/apps/openrct2.png
%{_datadir}/icons/hicolor/128x128/apps/openrct2.png
%{_datadir}/icons/hicolor/256x256/apps/openrct2.png
%{_datadir}/icons/hicolor/scalable/apps/openrct2.svg

%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*.xml

%{_datadir}/man/man6/*

%changelog
