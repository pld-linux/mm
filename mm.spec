Summary:	MM - Shared Memory Library
Summary(pl):	MM - Biblioteka dzielonej pamiêci
Name:		mm
Version:	1.3.0
Release:	1
Group:		Libraries
License:	BSD-like (see LICENSE)
Vendor:		Ralf S. Engelschall <rse@engelschall.com>
Source0:	ftp://ftp.ossp.org/pkg/lib/mm/%{name}-%{version}.tar.gz
# Source0-md5: 4bf43697983bf585905ee9a14b00dc32
URL:		http://www.engelschall.com/sw/mm/
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libmm1

%description
The MM library is a 2-layer abstraction library which simplifies the
usage of shared memory between forked (and this way strongly related)
processes under Unix platforms. On the first (lower) layer it hides
all platform dependent implementation details (allocation and locking)
when dealing with shared memory segments and on the second (higher)
layer it provides a high-level malloc(3)-style API for a convenient
and well known way to work with data-structures inside those shared
memory segments.

%description -l pl
MM jest 2-warstwow±, abstrakcyjn± bibliotek± upraszczaj±c± korzystanie
z pamiêci dzielonej pomiêdzy rozga³êzionymi (i w ten sposób mocno
powi±zanymi) procesami na platformach uniksowych. Pierwsza warstwa
(ni¿sza) ukrywa wszystkie szczegó³y zale¿ne od platformy (alokacja i
blokowanie) przy obs³udze segmentów pamiêci dzielonej. Druga (wy¿sza)
warstwa udostêpnia wysokopoziomowe API podobne do malloc(3)
umo¿liwiaj±ce wygodn± pracê ze strukturami danych w tych segmentach
pamiêci dzielonej.

%package devel
Summary:	Header files and development documentation for mm
Summary(pl):	Pliki nag³ówkowe i dokumentacja do mm
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libmm1-devel

%description devel
Header files and development documentation for mm.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do biblioteki mm.

%package static
Summary:	Static mm libraries
Summary(pl):	Biblioteki statyczne mm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static mm libraries.

%description static -l pl
Biblioteki statyczne mm.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README THANKS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mm-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a
