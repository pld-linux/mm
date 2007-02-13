Summary:	MM - Shared Memory Library
Summary(pl.UTF-8):	MM - Biblioteka dzielonej pamięci
Name:		mm
Version:	1.4.2
Release:	1
License:	BSD-like (see LICENSE)
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/mm/%{name}-%{version}.tar.gz
# Source0-md5:	bdb34c6c14071364c8f69062d2e8c82b
URL:		http://www.engelschall.com/sw/mm/
BuildRequires:	automake
BuildRequires:	libtool
Obsoletes:	libmm1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MM library is a 2-layer abstraction library which simplifies the
usage of shared memory between forked (and this way strongly related)
processes under Unix platforms. On the first (lower) layer it hides
all platform dependent implementation details (allocation and locking)
when dealing with shared memory segments and on the second (higher)
layer it provides a high-level malloc(3)-style API for a convenient
and well known way to work with data-structures inside those shared
memory segments.

%description -l pl.UTF-8
MM jest 2-warstwową, abstrakcyjną biblioteką upraszczającą korzystanie
z pamięci dzielonej pomiędzy rozgałęzionymi (i w ten sposób mocno
powiązanymi) procesami na platformach uniksowych. Pierwsza warstwa
(niższa) ukrywa wszystkie szczegóły zależne od platformy (alokacja i
blokowanie) przy obsłudze segmentów pamięci dzielonej. Druga (wyższa)
warstwa udostępnia wysokopoziomowe API podobne do malloc(3)
umożliwiające wygodną pracę ze strukturami danych w tych segmentach
pamięci dzielonej.

%package devel
Summary:	Header files and development documentation for mm
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do mm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libmm1-devel

%description devel
Header files and development documentation for mm.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do biblioteki mm.

%package static
Summary:	Static mm libraries
Summary(pl.UTF-8):	Biblioteki statyczne mm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static mm libraries.

%description static -l pl.UTF-8
Biblioteki statyczne mm.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_libdir}/lib*.a
