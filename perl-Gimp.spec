%define	module	Gimp
%define	pre	pre1
Summary:	Perl module enabling to write plugins for the Gimp2
Name:		perl-%{module}
Epoch:		1
Version:	2.2
Release:	0.%{pre}.11
License:	GPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Source0:	http://search.cpan.org/CPAN/authors/id/S/SJ/SJBURGES/%{module}-%{version}%{pre}.tar.bz2
Patch0:		Gimp-2.0pre1-fix-build.patch
Patch1:		Gimp-2.2-fix-str-fmt.patch
URL:		http://search.cpan.org/~sjburges/Gimp/Gimp.pm
BuildRequires:	pkgconfig(gtk+-2.0) perl-devel pkgconfig(gimp-2.0)
BuildRequires:	perl-Gtk2 perl-PDL perl-Parse-RecDescent perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:  pkgconfig(glitz)
Requires:	perl-PDL
%rename		gimp-perl

# Don't use automatic requires for perl-PDL (#22095):
%define _requires_exceptions perl(PDL

%description
This module provides perl access to the Gimp2 libraries.

%prep
%setup -q -n gimp-perl
%patch0 -p0
%patch1 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
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
