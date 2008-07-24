%define real_name LWPx-TimedHTTP

Summary:	LWPx::TimedHTTP - time the different stages of an HTTP request 
Name:		perl-%{real_name}
Version:	1.5
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SI/SIMONW/%{real_name}-%{version}.tar.bz2
Buildrequires: perl-devel
Buildrequires: perl-Module-Build
Buildrequires: perl-libwww-perl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module performs an HTTP request exactly the same as LWP does
normally except for the fact that it times each stage of the
request and then inserts the results as header. It's useful for
debugging where abouts in a connection slow downs are occuring.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}

install -d %{buildroot}%{perl_vendorlib}/LWPx
install -d %{buildroot}%{_mandir}/man3/

install -m0644 blib/lib/LWPx/TimedHTTP.pm %{buildroot}%{perl_vendorlib}/LWPx/
install -m0644 blib/libdoc/LWPx::TimedHTTP.3pm %{buildroot}%{_mandir}/man3/

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%dir %{perl_vendorlib}/LWPx
%{perl_vendorlib}/LWPx/TimedHTTP.pm
%{_mandir}/*/*

