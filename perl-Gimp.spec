%define module Gimp
%define pre pre1

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
Release:	0.%{pre}.13
License:	GPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://search.cpan.org/~sjburges/Gimp/Gimp.pm
Source0:	http://search.cpan.org/CPAN/authors/id/S/SJ/SJBURGES/%{module}-%{version}%{pre}.tar.bz2
Patch0:		Gimp-2.0pre1-fix-build.patch
Patch1:		Gimp-2.2-fix-str-fmt.patch
Patch2:		gimp-perl-headers.patch
Patch3:		Gimp-2.2-fix-includes.patch
Patch4:		Gimp-2.2-fix-gtk.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(gimp-2.0)
BuildRequires:	perl-Gtk2
BuildRequires:	perl-PDL
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	pkgconfig(glitz)
Requires:	perl-PDL
%rename	gimp-perl

%description
This module provides perl access to the Gimp2 libraries.

%prep
%setup -qn gimp-perl
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export CFLAGS="%{optflags} -I/usr/include/gtk-2.0"
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
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_libdir}/gimp/2.0/plug-ins/*
%{_prefix}/lib/perl5/*
#%{perl_vendorlib}/%{module}
#%{perl_vendorlib}/%{module}.pm
#%{perl_vendorlib}/auto/*

