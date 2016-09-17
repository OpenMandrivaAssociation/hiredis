%define major 0
%define minor 13
%define libname %mklibname hiredis %{major}.%{minor}
%define develname %mklibname hiredis -d

Summary:	A minimalistic C client library for Redis
Name:		hiredis
Version:	0.13.3
Release:	1
Group:		System/Libraries
License:	BSD
URL:		https://github.com/redis/hiredis/
Source0:	https://github.com/redis/hiredis/archive/v%{version}.tar.gz

%description 
Hiredis is a minimalistic C client library for the Redis database.

%package -n	%{libname}
Summary:        A minimalistic C client library for Redis
Group:          System/Libraries

%description -n	%{libname}
Hiredis is a minimalistic C client library for the Redis database.

%package -n	%{develname}
Summary:        Header files and libraries for hiredis C development
Group:          Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	hiredis-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the header files and libraries to develop applications
using a Redis database.

%prep
%setup -q

%build
%make OPTIMIZATION="%{optflags}" LDFLAGS="%{ldflags}" CC=%{__cc}

%install
make install PREFIX=%{buildroot}/%{_prefix} INSTALL_LIBRARY_PATH=%{buildroot}%{_libdir}

rm -f `find %{buildroot} -name *.*a`

%files -n %{libname}
%doc COPYING
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc README.md
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/*.so
