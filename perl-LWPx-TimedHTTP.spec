%define real_name LWPx-TimedHTTP
%define upstream_version 1.8

Summary:	LWPx::TimedHTTP - time the different stages of an HTTP request 
Name:		perl-%{real_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://www.cpan.org/authors/id/S/SI/SIMONW/LWPx-TimedHTTP-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(HTTP::Daemon)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl-libwww-perl
BuildArch:	noarch

%description
This module performs an HTTP request exactly the same as LWP does
normally except for the fact that it times each stage of the
request and then inserts the results as header. It's useful for
debugging where abouts in a connection slow downs are occuring.

%prep
%setup -q -n %{real_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
install -d %{buildroot}%{perl_vendorlib}/LWPx
install -d %{buildroot}%{_mandir}/man3/

install -m0644 blib/lib/LWPx/TimedHTTP.pm %{buildroot}%{perl_vendorlib}/LWPx/
install -m0644 blib/libdoc/LWPx::TimedHTTP.3pm %{buildroot}%{_mandir}/man3/

%files
%doc Changes
%dir %{perl_vendorlib}/LWPx
%{perl_vendorlib}/LWPx/TimedHTTP.pm
%{_mandir}/*/*

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.5-5mdv2010.0
+ Revision: 430484
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.5-4mdv2009.0
+ Revision: 257682
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.5-3mdv2009.0
+ Revision: 245730
- rebuild

* Sat Feb 02 2008 Funda Wang <fwang@mandriva.org> 1.5-1mdv2008.1
+ Revision: 161383
- update to new version 1.5

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-5mdv2008.0
+ Revision: 86527
- rebuild


* Mon Oct 17 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.4-4mdk
- Fix BuildRequires

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.4-3mdk
- Buildrequires fix

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.4-2mdk
- fix buildrequires

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4-1mdk
- initial Mandriva package


