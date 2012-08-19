#
# Conditional build:
%bcond_with	tests		# don't build and run tests

%define		plugin	skype-notifier
%include	/usr/lib/rpm/macros.java
Summary:	Jenkins Skype notifier plugin
Name:		jenkins-plugin-%{plugin}
Version:	1.1.0
Release:	0.1
License:	MIT License
Group:		Networking/Daemons/Java/Servlets
Source0:	https://github.com/jenkinsci/skype-im-plugin/tarball/skype-notifier-%{version}/%{name}-%{version}.tgz
# Source0-md5:	61aa40c39b2d915c4acb889359f6b412
URL:		https://wiki.jenkins-ci.org/display/JENKINS/Skype+Plugin
BuildRequires:	jpackage-utils
BuildRequires:	maven >= 2
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	java-skype
Requires:	jenkins
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		jenkinsdir	/usr/share/jenkins
%define		pluginsdir	%{jenkinsdir}/WEB-INF/plugins

%description
Integrates Jenkins with Skype for instant messaging.

%prep
%setup -qc
mv jenkinsci-skype-im-plugin-*/* .

%undos README

%build
export JAVA_HOME="%{java_home}"

mvn package \
%if %{without tests}
	-Dmaven.test.skip=true -DskipTests=true
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{pluginsdir}
cp -p target/*.hpi $RPM_BUILD_ROOT%{pluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{pluginsdir}/%{plugin}.hpi
