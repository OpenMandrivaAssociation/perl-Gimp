%define	upstream_name	 Gimp
%define upstream_version 2.3

%define __noautoreq 'perl\\(PDL(.*)\\)'

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3
Epoch:      1

Summary:    Perl module enabling to write plugins for the Gimp2

License:    GPL or Artistic
Group:      Development/GNOME and GTK+
Source0:    http://search.cpan.org/CPAN/authors/id/S/SJ/SJBURGES/%upstream_name-%{upstream_version}.tar.gz
Patch1:     Gimp-2.2-fix-str-fmt.patch
Patch2:     Gimp-2.2-linkage.patch
Url:        http://search.cpan.org/~sjburges/Gimp/Gimp.pm

BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: perl-devel
BuildRequires: pkgconfig(gimp-2.0)
BuildRequires: perl-Gtk2
BuildRequires: perl-PDL
BuildRequires: perl-Parse-RecDescent
BuildRequires: perl-ExtUtils-Depends
BuildRequires: perl-ExtUtils-PkgConfig
BuildRequires: pkgconfig(glitz)
Requires:      perl-PDL
%rename        gimp-perl

%description
This module provides perl access to the Gimp2 libraries.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch1 -p0
%patch2 -p0

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
%doc AUTHORS COPYING ChangeLog Changes MAINTAINERS META.json META.yml MYMETA.yml NEWS README TODO UI examples
%{_bindir}/*
%{_mandir}/*/*
%{_libdir}/gimp/2.0/plug-ins/*
%{_prefix}/lib/perl5/*

