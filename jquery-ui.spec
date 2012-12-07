Summary:	jQuery UI
Name:		jquery-ui
Version:	1.8.24
Release:	1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	http://jquery-ui.googlecode.com/files/%{name}-%{version}.zip
# Source0-md5:	22fdebda6ebd3210f78e370e39d25c0c
Source1:	find-lang.sh
URL:		http://jqueryui.com/
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	unzip
Requires:	jquery >= 1.4
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
Summary:	Demo for jQuery UI
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery UI
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery UI.

%package doc
Summary:	Manual for jQuery UI.
Summary(fr.UTF-8):	Documentation pour jQuery UI
Summary(it.UTF-8):	Documentazione di jQuery UI
Summary(pl.UTF-8):	Podręcznik dla jQuery UI
Group:		Documentation

%description doc
Documentation for jQuery UI.

%description doc -l fr.UTF-8
Documentation pour jQuery UI.

%description doc -l it.UTF-8
Documentazione di jQuery UI.

%description doc -l pl.UTF-8
Dokumentacja do jQuery UI.

%prep
%setup -q
%undos -f js,css,html

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
%{_appdir}/jquery.ui.*.js
%{_appdir}/jquery.effects.*.js
%{_appdir}/themes

# bundle of all effects
%{_appdir}/jquery-ui.js
# bundle of all languages
%{_appdir}/i18n/jquery-ui-i18n.js

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files doc
%doc docs/*
