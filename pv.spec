%bcond_without	uclibc

Summary:	Monitor the progress of data through a pipe
Name:		pv
Version:	1.4.12
Release:	5
Group:		Development/Other
License:	Artistic
Url:		http://www.ivarch.com/programs/pv.shtml
Source0:	http://www.ivarch.com/programs/sources/%{name}-%{version}.tar.bz2
Patch0:		pv-1.4.4-wholeprogram.patch
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

%prep
%setup -q
%apply_patches

%build
CONFIGURE_TOP="$PWD"
%if %{with uclibc}
mkdir -p uclibc
pushd uclibc
%uclibc_configure
%make WHOLE_PROGRAM=1
popd
%endif

mkdir -p system
pushd system
%configure2_5x
%make WHOLE_PROGRAM=1
popd

%check
%make -C system test WHOLE_PROGRAM=1

%install
%if %{with uclibc}
%makeinstall_std -C uclibc WHOLE_PROGRAM=1
%endif

%makeinstall_std -C system WHOLE_PROGRAM=1

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

