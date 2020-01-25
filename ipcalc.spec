Summary:	Address format change and calculation utility
Summary(pl.UTF-8):	Narzędzie do zmiany formatu i przeliczania adresów
Name:		ipcalc
Version:	0.41
Release:	1
License:	GPL v2+
Group:		Networking/Utilities
Source0:	http://jodies.de/ipcalc-archive/%{name}-%{version}.tar.gz
# Source0-md5:	fb791e9a5220fc8e624d915e18fc4697
URL:		http://jodies.de/ipcalc/
BuildRequires:	rpm-perlprov
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}/ipv4calc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog contributors
%attr(755,root,root) %{_bindir}/ipv4calc
