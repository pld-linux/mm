Summary:	MM - Shared Memory Library
Summary(pl):	MM - Biblioteka dzielonej pamiÍci
Name:		mm
Version:	1.1.3
Release:	4
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
License:	BSD-style (see LICENSE file)
Vendor:		Ralf S. Engelschall <rse@engelschall.com>
Source0:	http://www.engelschall.com/sw/mm/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
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
z pamiÍci dzielonej pomiÍdzy sforkowanymi (i w ten sposÛb mocno
powi±zanymi) procesami na platformach uniksowych. Pierwsza warstwa
(niøsza) ukrywa wszystkie szczegÛ≥y zaleøne od platformy (alokacja i
blokowanie) przy obs≥udze segmentÛw pamiÍci dzielonej. Druga (wyøsza)
warstwa daje wysokopoziomowe API podobne do malloc(3) aby wygodnie
pracowaÊ ze strukturami danych w tych segmentach pamiÍci dzielonej.

%package devel
Summary:	Header files and development documentation for mm
Summary(pl):	Pliki nag≥Ûwkowe i dokumentacja do mm
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Obsoletes:	libmm1-devel

%description devel
Header files and development documentation for mm.

%description -l pl devel
Pliki nag≥Ûwkowe i dokumentacja do biblioteki mm.

%package static
Summary:	Static mm libraries
Summary(pl):	Biblioteki statyczne mm
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static mm libraries.

%description -l pl static
Biblioteki statyczne mm.

%prep
%setup -q
%patch -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
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
