%define major 0
%define libname %mklibname hiredis %{major}
%define develname %mklibname hiredis -d

Summary:	A minimalistic C client library for Redis
Name:		hiredis
Version:	0.10.1
Release:	2
Group:		System/Libraries
License:	BSD
URL:		https://github.com/antirez/hiredis
Source0:	antirez-%{name}-v%{version}-28-gd5d8843.tar.gz

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

%setup -q -n antirez-%{name}-d5d8843

%build
%make OPTIMIZATION="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

make install PREFIX=%{buildroot}/%{_prefix} INSTALL_LIBRARY_PATH=%{buildroot}%{_libdir}

rm -f `find %{buildroot} -name *.*a`

%files -n %{libname}
%doc COPYING
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc README.md
%{_includedir}/%{name}
%{_libdir}/*.so



%changelog
* Mon Jan 30 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.1-1
+ Revision: 769814
- import hiredis


* Mon Jan 30 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.1-1
- fedora adopt
