%define upstream_name    HTML-FormHandler
%define upstream_version 0.36003

# Required but not provided with internal dep. generator
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(HTML::FormHandler::Meta::Role\\)'
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	An HTML form handler written in Moose
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::Strptime)
BuildRequires:	perl(Email::Valid)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Locale::Maketext)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Getopt)
BuildRequires:	perl(MooseX::Traits)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(MooseX::Types::Common)
BuildRequires:	perl(MooseX::Types::LoadableClass)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Memory::Cycle)
BuildRequires:	perl(HTML::TreeBuilder)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(aliased)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(File::ShareDir::Install)
BuildArch:	noarch

%description
HTML::FormHandler maintains a clean separation between form construction
and form rendering. It allows you to define your forms and fields in a
number of flexible ways. Although it provides renderers for HTML, you can
define custom renderers for any kind of presentation.

Although documentation in this file provides some overview, it is mainly
intended for API documentation. See the HTML::FormHandler::Manual::Intro
manpage for a more detailed introduction.

HTML::FormHandler allows you to define form fields and validators. It can
be used for both database and non-database forms, and will automatically
update or create rows in a database. It can be used to process structured
data that doesn't come from an HTML form.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.340.10-1mdv2011.0
+ Revision: 677432
- update to new version 0.34001

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.330.20-2
+ Revision: 657337
- rebuild for updated spec-helper

* Thu Feb 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.330.20-1
+ Revision: 639638
- update to new version 0.33002
- update to new version 0.32005

* Mon Aug 02 2010 Shlomi Fish <shlomif@mandriva.org> 0.320.20-1mdv2011.0
+ Revision: 565113
- Upgraded to 0.32002

* Tue Jul 27 2010 Shlomi Fish <shlomif@mandriva.org> 0.320.10-1mdv2011.0
+ Revision: 561062
- import perl-HTML-FormHandler


* Thu Jul 15 2010 cpan2dist 0.32001-1mdv
- initial mdv release, generated with cpan2dist
