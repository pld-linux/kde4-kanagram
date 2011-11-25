%define		_state		stable
%define		qtver		4.7.4

Summary:	K Desktop Environment - Guess anagram game
Summary(pl.UTF-8):	K Desktop Environment - Gra w zgadywanie anagramów
Name:		kanagram
Version:	4.7.3
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	b17de32ea9e22738c773b3188128609d
URL:		http://www.kde.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libkdeedu-devel >= %{version}
Requires:	kde4-kdebase >= %{version}
Obsoletes:	kde4-kdeedu-kanagram < 4.6.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guess anagram game.

%description -l pl.UTF-8
Gra w zgadywanie anagramw.

%prep
%setup -q

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kanagram
%{_datadir}/apps/kanagram
%{_datadir}/config/kanagram.knsrc
%{_datadir}/config.kcfg/kanagram.kcfg
%{_desktopdir}/kde4/kanagram.desktop
%{_iconsdir}/hicolor/scalable/apps/kanagram.svgz
%{_iconsdir}/hicolor/*x*/apps/kanagram.png
