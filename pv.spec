%define _disable_lto 1

Summary:	Monitor the progress of data through a pipe
Name:		pv
Version:	1.5.7
Release:	7
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

%description
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
%configure

%make

%check
%make test

%install
%makeinstall_std -C system

%find_lang %{name}

# note; the nls files should probably be added also somehow in the future...
%files -f %{name}.lang
%doc README
%{_bindir}/pv
%{_mandir}/man1/pv.1*
