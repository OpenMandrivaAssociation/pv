Summary:	Monitor the progress of data through a pipe.
Name:		pv
Version:	0.8.6
Release:	%mkrel 5
Group:		Development/Other
License:	Artistic
URL:		http://www.ivarch.com/programs/pv.shtml
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	gettext-devel
BuildRequires:	gettext
BuildRequires:	tetex
BuildRequires:	texinfo
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_infodir}
install -d %{buildroot}%{_mandir}/man1

%{makeinstall_std}

# prepare for html doc inclusion
mkdir html; cp doc/*.html html/

%find_lang %{name}
# note; the nls files should probably be added also somehow in the future...

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post
%_install_info %{name}.info

%postun
%_remove_install_info %{name}.info

%files -f %{name}.lang
%defattr(-, root, root)
%doc html README doc/NEWS doc/TODO doc/COPYING
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man1/*


