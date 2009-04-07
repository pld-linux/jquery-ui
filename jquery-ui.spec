Summary:	jQuery UI
Name:		jquery-ui
Version:	1.5.3
Release:	0.1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	http://jquery-ui.googlecode.com/files/%{name}-%{version}.zip
# Source0-md5:	5fc1bdd91953e975411de0623e4b0302
URL:		http://jqueryui.com/
BuildRequires:	rpmbuild(macros) > 1.268
Source1:	%{name}-find-lang.sh
Requires:	jquery >= 1.2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/jquery/ui

%description
jQuery UI provides abstractions for low-level interaction and
high-level, themeable widgets, built on top of the jQuery JavaScript
Library, that you can use to build highly interactive web
applications.

%package demo
Summary:	Demo for %{name}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu %{name}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q

find '(' -name '*.js' -o -name '*.html' ')' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

install %{SOURCE1} find-lang.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -a ui/* $RPM_BUILD_ROOT%{_appdir}
cp -a demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

./find-lang.sh %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_appdir}
%{_appdir}/*.js
%{_appdir}/packed
%{_appdir}/minified

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
