%define upstream_name    HTML-FormHandler
%define upstream_version 0.33002

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    An HTML form handler written in Moose
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::Strptime)
BuildRequires: perl(Email::Valid)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Locale::Maketext)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Getopt)
BuildRequires: perl(MooseX::Traits)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(MooseX::Types::Common)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(aliased)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(File::ShareDir::Install)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


