Summary:	MM - Shared Memory Library
Name:		mm
Version:	1.0.12
Release:	1
Group:		Libraries
Group(pl):	Biblioteki
Copyright:	BSD-style (see LICENSE file)
Vendor:		Ralf S. Engelschall <rse@engelschall.com>
Source:		http://www.engelschall.com/sw/mm/%{name}-%{version}.tar.gz
Patch:		mm-DESTDIR.patch
URL:		http://www.engelschall.com/sw/mm/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MM library is a 2-layer abstraction library which simplifies the usage
of shared memory between forked (and this way strongly related) processes
under Unix platforms. On the first (lower) layer it hides all platform
dependent implementation details (allocation and locking) when dealing with
shared memory segments and on the second (higher) layer it provides a
high-level malloc(3)-style API for a convenient and well known way to work
with data-structures inside those shared memory segments.

%package devel
Summary:	Header files and development documentation for mm
Summary(pl):	Pliki nag³ówkowe i dokumentacja do mm
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for mm.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do biblioteki mm.

%package static
Summary:	Static mm libraries
Summary(pl):	Biblioteki statyczne mm
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static mm libraries.

%description -l pl static
Biblioteki statyczne mm.

%prep
%setup -q
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT/%{_mandir}/man?/* \
	CHANGES README LICENSE

%find_lang %{name}

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
%attr(644,root,root) %{_libdir}/lib*.a

%changelog
