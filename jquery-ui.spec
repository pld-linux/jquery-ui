Summary:	jQuery UI
Name:		jquery-ui
Version:	1.7.2
Release:	1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	http://jquery-ui.googlecode.com/files/%{name}-%{version}.zip
# Source0-md5:	ac7986a8caedf11c4392ad4964c5d5af
URL:		http://jqueryui.com/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Source1:	find-lang.sh
Requires:	jquery >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/jquery/ui

%define		find_lang 	sh %{SOURCE1} %{buildroot}

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

find ui/minified -name '*.min.js' | while read a; do
	mv $a ${a%.min.js}.js
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -a ui/minified/* $RPM_BUILD_ROOT%{_appdir}
cp -a themes $RPM_BUILD_ROOT%{_appdir}
cp -a demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.txt
%dir %{_appdir}
%{_appdir}/ui.*.js
%{_appdir}/effects.*.js
%{_appdir}/themes

# bundle of all effects
%{_appdir}/jquery-ui.js
# bundle of all languages
%{_appdir}/i18n/jquery-ui-i18n.js

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
