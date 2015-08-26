%bcond_with	uclibc

Summary:	Monitor the progress of data through a pipe
Name:		pv
Version:	1.5.7
Release:	4
Group:		Development/Other
License:	Artistic
Url:		http://www.ivarch.com/programs/pv.shtml
Source0:	http://www.ivarch.com/programs/sources/%{name}-%{version}.tar.bz2
#(tpg) clang does not recognize fwhole-program
#Patch0:		pv-1.4.4-wholeprogram.patch
BuildRequires:	gettext
BuildRequires:	tetex
BuildRequires:	texinfo
BuildRequires:	gettext-devel
%if %{with uclibc}
BuildRequires:	uClibc-devel
%endif

%description
PV ("Pipe Viewer") is a tool for monitoring the progress of data
through a pipeline.  It can be inserted into any normal pipeline
between two processes to give a visual indication of how quickly
data is passing through, how long it has taken, how near to
completion it is, and an estimate of how long it will be until
completion.

%if %{with uclibc}
%package -n	uclibc-%{name}
Summary:	Monitor the progress of data through a pipe (uClibc build)
Group:		Development/Other

%description -n	uclibc-%{name}
PV ("Pipe Viewer") is a tool for monitoring the progress of data
through a pipeline.  It can be inserted into any normal pipeline
between two processes to give a visual indication of how quickly
data is passing through, how long it has taken, how near to
completion it is, and an estimate of how long it will be until
completion.
%endif

%prep
%setup -q
%apply_patches

%build
CONFIGURE_TOP="$PWD"
%if %{with uclibc}
mkdir -p uclibc
pushd uclibc
#cb cant use uclibc_configure due to localedir
%configure2_5x \
--libdir=%{uclibc_root}%{_libdir} \
--prefix=%{uclibc_root}%{_prefix} \
--exec-prefix=%{uclibc_root}%{_prefix} \
--bindir=%{uclibc_root}%{_bindir} \
--sbindir=%{uclibc_root}%{_sbindir} \
--enable-nls \
--with-ncursesw \
--disable-rpath-hack \
--enable-static \
CC="%{uclibc_cc}" \
CXX="%{uclibc_cxx}" \
CFLAGS="%{uclibc_cflags}" \
CXXFLAGS="%{uclibc_cxxflags}"

%make
popd
%endif

mkdir -p system
pushd system
%configure

%make
popd

%check
%make -C system test

%install
%if %{with uclibc}
%makeinstall_std -C uclibc
%endif

%makeinstall_std -C system

%find_lang %{name}

# note; the nls files should probably be added also somehow in the future...
%files -f %{name}.lang
%doc README doc/NEWS doc/TODO doc/COPYING
%{_bindir}/pv
%{_mandir}/man1/pv.1*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}%{_bindir}/pv
%endif
