#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MasonX
%define		pnam	Interp-WithCallbacks
Summary:	MasonX::Interp::WithCallbacks - Mason callback support via Params::CallbackRequest
Summary(pl.UTF-8):	MasonX::Interp::WithCallbacks - obsługa callbacków Masona poprzez Params::CallbackRequest
Name:		perl-MasonX-Interp-WithCallbacks
Version:	1.13
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MasonX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cd0b2a49683d4c67fb2aa44dadedc42f
URL:		http://search.cpan.org/dist/MasonX-Interp-WithCallbacks/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Container >= 0.09
BuildRequires:	perl-HTML-Mason >= 1.23
BuildRequires:	perl-Params-CallbackRequest >= 1.11
BuildRequires:	perl-Test-Simple >= 0.17
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

%description -l pl.UTF-8
MasonX::Interp::WithCallbacks jest podklasą HTML::Mason::Interp
dostarczającą Masonowi system wywołań zwrotnych (callbacków) zbudowany
w oparciu o Params::CallbackRequest. Callbacki mogą być referencjami
do kodu przekazanymi do konstruktora new() lub metodami zdefiniowanymi
w podklasach Params::Callback. Wywołania zwrotne są wyzwalane albo dla
każdego żądania lub przez specjalnie nazwane klucze w argumentach
żądań Masona, zaraz przed tym, jak Mason tworzy i wykonuje stos
żądanych komponentów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/MasonX/Interp
%{perl_vendorlib}/MasonX/*/*.pm
%{_mandir}/man3/*
