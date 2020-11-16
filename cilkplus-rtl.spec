# requires language extension support in compiler (GCC >= 4.9 < 8, LLVM branch)
#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Intel(R) Cilk(TM) Plus Runtime Library
Summary(pl.UTF-8):	Biblioteka uruchomieniowa Intel(R) Cilk(TM) Plus
Name:		cilkplus-rtl
Version:	4516
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://www.cilkplus.org/download#runtime-sources
Source0:	https://www.cilkplus.org/sites/default/files/runtime_source/%{name}-00%{version}.tgz
# Source0-md5:	b43fd55f752704ec2e2c6b1cf02feccd
Patch0:		%{name}-link.patch
URL:		https://www.cilkplus.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	libstdc++-devel >= 6:4.9
BuildRequires:	libtool
ExclusiveArch:	%{ix86} %{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Cilk Plus C/C++ language extensions runtime
library.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę uruchomieniową rozszerzeń Cilk Plus dla
języków C/C++.

%package -n libcilkrts
Summary:	Intel(R) Cilk(TM) Plus Runtime Library
Summary(pl.UTF-8):	Biblioteka uruchomieniowa Intel(R) Cilk(TM) Plus
# there was 6:7.5.0 in gcc.spec
Epoch:		6
Group:		Libraries
%ifarch %{ix86}
Obsoletes:	libcilkrts-multilib-32 < 6:8.0
%endif
%ifarch %{x8664}
Obsoletes:	libcilkrts-multilib-64 < 6:8.0
%endif
%ifarch x32
Obsoletes:	libcilkrts-multilib-x32 < 6:8.0
%endif

%description -n libcilkrts
This package contains the Cilk Plus C/C++ language extensions runtime
library.

%description -n libcilkrts -l pl.UTF-8
Ten pakiet zawiera bibliotekę uruchomieniową rozszerzeń Cilk Plus dla
języków C/C++.

%package -n libcilkrts-devel
Summary:	Header files for Cilk Plus language extensions
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzeń Cilk Plus
Epoch:		6
Group:		Development/Libraries
Requires:	libcilkrts = %{version}-%{release}
%ifarch %{ix86}
Obsoletes:	libcilkrts-multilib-32-devel < 6:8.0
%endif
%ifarch %{x8664}
Obsoletes:	libcilkrts-multilib-64-devel < 6:8.0
%endif
%ifarch x32
Obsoletes:	libcilkrts-multilib-x32-devel < 6:8.0
%endif

%description -n libcilkrts-devel
This package contains development files for Cilk Plus C/C++ language
extensions.

%description -n libcilkrts-devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne rozszerzeń Cilk Plus dla
języków C/C++.

%package -n libcilkrts-static
Summary:	Cilk Plus language extensions static library
Summary(pl.UTF-8):	Biblioteka statyczna rozszerzeń Cilk Plus
Epoch:		6
Group:		Development/Libraries
Requires:	libcilkrts-devel = %{version}-%{release}
%ifarch %{ix86}
Obsoletes:	libcilkrts-multilib-32-static < 6:8.0
%endif
%ifarch %{x8664}
Obsoletes:	libcilkrts-multilib-64-static < 6:8.0
%endif
%ifarch x32
Obsoletes:	libcilkrts-multilib-x32-static < 6:8.0
%endif

%description -n libcilkrts-static
This package contains Cilk Plus C/C++ language extensions static
library.

%description -n libcilkrts-static -l pl.UTF-8
Ten pakiet zawiera bibliotekę statyczną rozszerzeń Cilk Plus dla
języków C/C++.

%prep
%setup -q -n %{name}-src-00%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libcilkrts -p /sbin/ldconfig
%postun	-n libcilkrts -p /sbin/ldconfig

%files -n libcilkrts
%defattr(644,root,root,755)
%doc README include/cilk/{mainpage.md,reducers.md}
%attr(755,root,root) %{_libdir}/libcilkrts.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcilkrts.so.5

%files -n libcilkrts-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcilkrts.so
%{_libdir}/libcilkrts.la
%{_includedir}/cilk

%if %{with static_libs}
%files -n libcilkrts-static
%defattr(644,root,root,755)
%{_libdir}/libcilkrts.a
%endif
