Summary:	Monitor the progress of data through a pipe
Name:		pv
Version:	1.4.4
Release:	1
Group:		Development/Other
License:	Artistic
URL:		http://www.ivarch.com/programs/pv.shtml
Source0:	http://www.ivarch.com/programs/sources/%{name}-%{version}.tar.bz2
BuildRequires:	gettext-devel
BuildRequires:	gettext
BuildRequires:	tetex
BuildRequires:	texinfo

%description
PV ("Pipe Viewer") is a tool for monitoring the progress of data
through a pipeline.  It can be inserted into any normal pipeline
between two processes to give a visual indication of how quickly
data is passing through, how long it has taken, how near to
completion it is, and an estimate of how long it will be until
completion.

%prep

%setup -q

%build
%configure2_5x

%make

make test

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

%{makeinstall_std}

%find_lang %{name}
# note; the nls files should probably be added also somehow in the future...
%files -f %{name}.lang
%doc README doc/NEWS doc/TODO doc/COPYING
%{_bindir}/*
%{_mandir}/man1/*
