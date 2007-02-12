#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	Infinite
Summary:	Set::Infinite - Sets of intervals
Summary(pl.UTF-8):	Set::Infinite - zbiory przedziałów
Name:		perl-Set-Infinite
Version:	0.61
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c9912f4ee6ac2e2291be94a5a2bd11f2
URL:		http://search.cpan.org/dist/Set-Infinite/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::Infinite is a Set Theory module for infinite sets.

A set is a collection of objects. The objects that belong to a set are
called its members, or "elements".

As objects we allow (almost) anything: reals, integers, and objects
(such as dates).

We allow sets to be infinite.

There is no account for the order of elements. For example, {1,2} =
{2,1}.

%description -l pl.UTF-8
Set::Infinite to moduł teorii zbiorów dla zbiorów nieskończonych.

Zbiór to kolekcja obiektów. Obiekty należące do zbioru są nazywane
jego elementami.

Jako obiekty dopuszczone jest (prawie) wszystko: liczby rzeczywiste,
całkowite i obiekty (takie jak daty).

Ten moduł dopuszcza zbiory nieskończone.

Nie ma porządku elementów. Na przykład {1,2} = {2,1}.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Set/*.pm
%{perl_vendorlib}/Set/Infinite
%{_mandir}/man3/*
