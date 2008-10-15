Summary:	jQuery UI
Name:		jquery-ui
Version:	1.5.2
Release:	0.1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	http://jquery-ui.googlecode.com/files/jquery.ui-%{version}.zip
# Source0-md5:	65278dc21201ecf92c67406f2952de1e
URL:		http://ui.jquery.com/
BuildRequires:	rpmbuild(macros) > 1.268
Requires:	webserver(access)
Requires:	webserver(alias)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{name}

%description
jQuery UI provides abstractions for low-level interaction and
high-level, themeable widgets, built on top of the jQuery JavaScript
Library, that you can use to build highly interactive web
applications.

%prep
%setup -q -n jquery.ui-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
