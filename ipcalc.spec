Summary:	Address format change and calculation utility
Summary(pl.UTF-8):	Narzędzie do zmiany formatu i przeliczania adresów
Name:		ipcalc
Version:	1.0.3
Release:	1
License:	GPL v2+
Group:		Networking/Utilities
#Source0Download: https://gitlab.com/ipcalc/ipcalc/-/tags
Source0:	https://gitlab.com/ipcalc/ipcalc/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	fa2544da2635894158196da401e3eb8c
URL:		https://gitlab.com/ipcalc/ipcalc
BuildRequires:	libmaxminddb-devel
BuildRequires:	meson >= 0.49
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	ronn
BuildRequires:	rpmbuild(macros) >= 1.726
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ipcalc takes an IP address and netmask and calculates the resulting
broadcast, network, Cisco wildcard mask, and host range. By giving a
second netmask, you can design sub- and supernetworks. It is also
intended to be a teaching tool and presents the results as
easy-to-understand binary values.

%description -l pl.UTF-8
ipcalc pobiera adres IP oraz maskę sieci i oblicza wynikający z nich
adres sieci, broadcastu, maskę wildcard dla Cisco i zakres hostów.
Podając drugą maskę, możesz projektować pod- i nadsieci. Program ten
ma być także narzędziem do nauki i prezentuje wyniki w łatwej do
zrozumienia binarnej postaci.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/bin

%meson_install

%{__mv} $RPM_BUILD_ROOT{%{_bindir},/bin}/ipcalc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md NEWS
%attr(755,root,root) /bin/ipcalc
%{_mandir}/man1/ipcalc.1*
