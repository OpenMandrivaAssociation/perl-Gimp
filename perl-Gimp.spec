%define	module	Gimp
%define pre pre1
Summary:	Perl module enabling to write plugins for the Gimp2
Name:		perl-%module
Epoch:		1
Version:	2.2
Release:	%mkrel 0.%pre.4
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Source0:	http://search.cpan.org/CPAN/authors/id/S/SJ/SJBURGES/%module-%{version}%pre.tar.bz2
Patch0:		Gimp-2.0pre1-fix-build.patch
URL:		http://search.cpan.org/~sjburges/Gimp/Gimp.pm
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel perl-devel libgimp-devel > 2.0
BuildRequires:	perl-Gtk2 perl-PDL perl-Parse-RecDescent perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:  glitz-devel
Requires:	perl-PDL
Requires:	gtk+2 libgtk+2, perl-Glib >= 1.021
Provides:	gimp-perl = %epoch:%version
Obsoletes:	gimp-perl < %epoch:2.0

# Don't use automatic requires for perl-PDL (#22095):
%define _requires_exceptions perl(PDL

%description
This module provides perl access to the Gimp2 libraries.

%prep
%setup -q -n gimp-perl
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gimp/2.0/plug-ins/
make DESTDIR=%buildroot pure_vendor_install
install -m 755 examples/* $RPM_BUILD_ROOT%{_libdir}/gimp/2.0/plug-ins/
perl -pi -e "s^/opt/bin/perl^%_bindir/perl^" $RPM_BUILD_ROOT%{_libdir}/gimp/2.0/plug-ins/*

# fix conflict with gimp-1:
rm -f $RPM_BUILD_ROOT%_mandir/man1/embedxpm.*
rm -f $RPM_BUILD_ROOT%{_libdir}/gimp/2.0/plug-ins/redeye
rm -f $RPM_BUILD_ROOT%{_libdir}/gimp/2.0/plug-ins/README
rm -f $RPM_BUILD_ROOT%{_libdir}/gimp/2.0/plug-ins/examples.TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING* examples/examples.TODO examples/README
%_bindir/*
%_mandir/*/*
%_libdir/gimp/2.0/plug-ins/*
%_prefix/lib/perl5/*
#%{perl_vendorlib}/%module
#%{perl_vendorlib}/%module.pm
#%{perl_vendorlib}/auto/*

