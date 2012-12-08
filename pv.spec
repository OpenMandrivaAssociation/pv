Summary:	Monitor the progress of data through a pipe
Name:		pv
Version:	1.1.4
Release:	%mkrel 6
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
install -d %{buildroot}%{_mandir}/man1

%{makeinstall_std}

%find_lang %{name}
# note; the nls files should probably be added also somehow in the future...

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc README doc/NEWS doc/TODO doc/COPYING
%{_bindir}/*
%{_mandir}/man1/*




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-4mdv2011.0
+ Revision: 667898
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-3mdv2011.0
+ Revision: 607244
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-2mdv2010.1
+ Revision: 523739
- rebuilt for 2010.1

* Sat Feb 14 2009 Pascal Terjan <pterjan@mandriva.org> 1.1.4-1mdv2009.1
+ Revision: 340179
- Update to current version

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.8.6-6mdv2009.0
+ Revision: 220246
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Mar 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-5mdv2007.1
+ Revision: 138895
- fix deps
- fix deps
- Import pv

* Fri Jan 19 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-4mdv2007.1
- rebuild

* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-3mdv2007.0
- rebuild

* Sat Aug 27 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-2mdk
- rebuild

* Thu Jul 29 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.8.6-1mdk
- 0.8.6

* Sun Jun 06 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.8.5-1mdk
- 0.8.5
- rebuilt against new deps and with gcc v3.4.x
- fix deps
- use macros

