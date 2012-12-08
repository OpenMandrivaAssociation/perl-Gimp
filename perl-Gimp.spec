%define	module	Gimp
%define	pre	pre1

# Don't use automatic requires for perl-PDL (#22095):
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(PDL(.*)\\)'
%else
%define _requires_exceptions perl(PDL
%endif

Summary:	Perl module enabling to write plugins for the Gimp2
Name:		perl-%{module}
Epoch:		1
Version:	2.2
Release:	0.%{pre}.12
License:	GPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Source0:	http://search.cpan.org/CPAN/authors/id/S/SJ/SJBURGES/%{module}-%{version}%{pre}.tar.bz2
Patch0:		Gimp-2.0pre1-fix-build.patch
Patch1:		Gimp-2.2-fix-str-fmt.patch
Patch2:		gimp-perl-headers.patch
URL:		http://search.cpan.org/~sjburges/Gimp/Gimp.pm
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(gimp-2.0)
BuildRequires:	perl-Gtk2
BuildRequires:	perl-PDL
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:  pkgconfig(glitz)
Requires:	perl-PDL
%rename		gimp-perl

%description
This module provides perl access to the Gimp2 libraries.

%prep
%setup -q -n gimp-perl
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
mkdir -p %{buildroot}%{_libdir}/gimp/2.0/plug-ins/
make DESTDIR=%{buildroot} pure_vendor_install
install -m 755 examples/* %{buildroot}%{_libdir}/gimp/2.0/plug-ins/
perl -pi -e "s^/opt/bin/perl^%{_bindir}/perl^" %{buildroot}%{_libdir}/gimp/2.0/plug-ins/*

# fix conflict with gimp-1:
rm -f %{buildroot}%{_mandir}/man1/embedxpm.*
rm -f %{buildroot}%{_libdir}/gimp/2.0/plug-ins/redeye
rm -f %{buildroot}%{_libdir}/gimp/2.0/plug-ins/README
rm -f %{buildroot}%{_libdir}/gimp/2.0/plug-ins/examples.TODO

%files
%doc AUTHORS examples/examples.TODO examples/README
%{_bindir}/*
%{_mandir}/*/*
%{_libdir}/gimp/2.0/plug-ins/*
%{_prefix}/lib/perl5/*
#%{perl_vendorlib}/%{module}
#%{perl_vendorlib}/%{module}.pm
#%{perl_vendorlib}/auto/*


%changelog
* Wed Feb 01 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 1:2.2-0.pre1.11
+ Revision: 770494
- default compile flags are already set by perl, so no need to set these ourself
- drop copyright docs, they're already provided with 'common-licenses'
- update license
- drop useless dependencies
- use pkgconfig() deps
- svn commit -m mass rebuild of perl extension against perl 5.14.2
- cleanups

  + Oden Eriksson <oeriksson@mandriva.com>
    - fix deps
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:2.2-0.pre1.8
+ Revision: 702771
- rebuilt against libpng-1.5.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:2.2-0.pre1.7
+ Revision: 667179
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1:2.2-0.pre1.6mdv2011.0
+ Revision: 564616
- rebuild for  perl 5.12.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:2.2-0.pre1.5mdv2011.0
+ Revision: 426447
- rebuild

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 1:2.2-0.pre1.4mdv2009.1
+ Revision: 366032
- fix str fmt

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1:2.2-0.pre1.3mdv2008.1
+ Revision: 151376
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Jul 18 2006 Götz Waschk <waschk@mandriva.org> 2.2-0.pre1.2mdv2007.0
- fix buildrequires

* Tue Jul 18 2006 Götz Waschk <waschk@mandriva.org> 2.2-0.pre1.1mdv2007.0
- fix conflict with gimp
- fix build
- new version

* Mon Apr 24 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.0-9mdk
- add bug reference

* Mon Apr 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:2.0-8mdk
- Don't use automatic requires for perl-PDL (#22095)

* Fri Dec 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.0-7mdk
- revert previous buildrequires

* Fri Dec 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.0-6mdk
- Fix Buildrequires

* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.0-5mdk
- Fix BuildRequires

* Wed Aug 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:2.0-4mdk
- Rebuild, fix installation process

* Mon Apr 18 2005 Giuseppe Ghibò <ghibo@mandriva.com> 1:2.0-3mdk
- Fixed X86-64 building.

* Tue Nov 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.0-2mdk
- rebuild for new perl

* Mon May 17 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.0-1mdk
- new release

* Tue Apr 20 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.0-0.pre2_4mdk
- even more buildrequires *grf*

* Mon Apr 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.0-0.pre2_3mdk
- whoppsy, yet another buildrequires caught!
- get rid of cvs files

* Mon Apr 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.0-0.pre2_2mdk
- fix buildrequires
- spec cosmetics

* Fri Mar 26 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.0-0.pre2_1mdk
- initial release

