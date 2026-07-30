%define real_name LWPx-TimedHTTP
Summary:	LWPx::TimedHTTP - time the different stages of an HTTP request 
Name:		perl-%{real_name}
Version:	1.8
Release:	1
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/LWPx-TimedHTTP
Source0:	https://cpan.metacpan.org/authors/id/S/SI/SIMONW/LWPx-TimedHTTP-1.8.tar.gz
BuildRequires:	make
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
%setup -q -n %{real_name}-%{version}

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

