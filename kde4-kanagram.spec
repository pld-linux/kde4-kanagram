%define		_state		stable
%define		orgname		kanagram
%define		qtver		4.8.0

Summary:	K Desktop Environment - Guess anagram game
Summary(pl.UTF-8):	K Desktop Environment - Gra w zgadywanie anagramów
Name:		kde4-kanagram
Version:	4.14.3
Release:	2
License:	GPL
Group:		X11/Applications/Science
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	059c37281e78a6e71f83896ea5c4a918
URL:		http://www.kde.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdeedu-devel >= %{version}
Requires:	kde4-kdebase >= %{version}
Obsoletes:	kde4-kdeedu-kanagram < 4.6.99
Obsoletes:	kanagram < 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guess anagram game.

%description -l pl.UTF-8
Gra w zgadywanie anagramów.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DGWENVIEW_SEMANTICINFO_BACKEND=Nepomuk \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%find_lang kanagram     --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kanagram
%{_datadir}/appdata/kanagram.appdata.xml
%{_datadir}/apps/kanagram
%{_datadir}/apps/plasma/packages/org.kde.kanagram
%{_datadir}/config/kanagram.knsrc
%{_datadir}/config.kcfg/kanagram.kcfg
%{_desktopdir}/kde4/kanagram.desktop
%{_iconsdir}/hicolor/scalable/apps/kanagram.svgz
%{_iconsdir}/hicolor/*x*/apps/kanagram.png
