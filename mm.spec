Summary:	MM - Shared Memory Library
Summary(pl):	MM - Biblioteka dzielonej pamiêci
Name:		mm
Version:	1.1.3
Release:	6
Group:		Libraries
License:	BSD-like (see LICENSE)
Vendor:		Ralf S. Engelschall <rse@engelschall.com>
Source0:	http://www.engelschall.com/sw/mm/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-tmpfile.patch
URL:		http://www.engelschall.com/sw/mm/
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
z pamiêci dzielonej pomiêdzy sforkowanymi (i w ten sposób mocno
powi±zanymi) procesami na platformach uniksowych. Pierwsza warstwa
(ni¿sza) ukrywa wszystkie szczegó³y zale¿ne od platformy (alokacja i
blokowanie) przy obs³udze segmentów pamiêci dzielonej. Druga (wy¿sza)
warstwa daje wysokopoziomowe API podobne do malloc(3) aby wygodnie
pracowaæ ze strukturami danych w tych segmentach pamiêci dzielonej.

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
%patch0 -p1
%patch1 -p1

%build
%configure2_13
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
%doc ChangeLog README LICENSE
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mm-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a
