#
# Conditional build:
%bcond_with	tests           # perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MasonX
%define	pnam	Interp-WithCallbacks
Summary:	MasonX::Interp::WithCallbacks - Mason callback support via Params::CallbackRequest
Summary(pl):	MasonX::Interp::WithCallbacks - obs³uga callbacków Masona poprzez Params::CallbackRequest
Name:		perl-MasonX-Interp-WithCallbacks
Version:	1.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0f0fa00e6a5d2c5318ad48ef9cea3705
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Container >= 0.09
BuildRequires:	perl-HTML-Mason >= 1.23
BuildRequires:	perl-Params-CallbackRequest >= 1.11
BuildRequires:	perl(Test::Simple) >= 0.17
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MasonX::Interp::WithCallbacks subclasses HTML::Mason::Interp
in order to provide a Mason callback system built on
Params::CallbackRequest. Callbacks may be either code references
provided to the new() constructor, or methods defined in subclasses of
Params::Callback. Callbacks are triggered either for every request or
by specially named keys in the Mason request arguments, and all
callbacks are executed at the beginning of a request, just before
Mason creates and executes the request component stack.

%description -l pl
MasonX::Interp::WithCallbacks jest podklas± HTML::Mason::Interp
dostarczaj±c± Masonowi system wywo³añ zwrotnych (callbacków) zbudowany
w oparciu o Params::CallbackRequest. Callbacki mog± byæ referencjami
do kodu przekazanymi do konstruktora new() lub metodami zdefiniowanymi
w podklasach Params::Callback. Wywo³ania zwrotne s± wyzwalane albo dla
ka¿dego ¿±dania lub przez specjalnie nazwane klucze w argumentach
¿±dañ Masona, zaraz przed tym, jak Mason tworzy i wykonuje stos
¿±danych komponentów.

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
%doc Changes README
%{perl_vendorlib}/MasonX/*/*.pm
%{_mandir}/man3/*
