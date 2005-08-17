%include /usr/lib/rpm/macros.perl
Summary:	Address format change and calculation utility
Summary(pl):	Narz�dzie do zmiany formatu i przeliczania adres�w
Name:		ipcalc
Version:	0.40
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://jodies.de/ipcalc-archive/%{name}-%{version}.tar.gz
# Source0-md5:	ad22070e7a784d83361b6bcf18dec7c1
URL:		http://jodies.de/ipcalc/
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ipcalc takes an IP address and netmask and calculates the resulting
broadcast, network, Cisco wildcard mask, and host range. By giving a
second netmask, you can design sub- and supernetworks. It is also
intended to be a teaching tool and presents the results as
easy-to-understand binary values.

%description -l pl
ipcalc pobiera adres IP oraz mask� sieci i oblicza wynikaj�cy z nich
adres sieci, broadcastu, mask� wildcard dla Cisco i zakres host�w.
Podaj�c drug� mask�, mo�esz projektowa� pod- i nadsieci. Program ten
ma by� tak�e narz�dziem do nauki i prezentuje wyniki w �atwej do
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
%doc changelog
%attr(755,root,root) %{_bindir}/ipv4calc
