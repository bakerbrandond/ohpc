#----------------------------------------------------------------------------bh-
# This RPM .spec file is part of the OpenHPC project.
#
# It may have been modified from the default version supplied by the underlying
# release package (if available) in order to apply patches, perform customized
# build/install configurations, and supply additional files to support
# desired integration conventions.
#
#----------------------------------------------------------------------------eh-

%{!?_rel:%{expand:%%global _rel 0.r%(test "1686" != "0000" && echo "1686" || svnversion | sed 's/[^0-9].*$//' | grep '^[0-9][0-9]*$' || git svn find-rev `git show -s --pretty=format:%h` || echo 0000)}}

%include %{_sourcedir}/OHPC_macros
%{!?PROJ_DELIM: %global PROJ_DELIM -ohpc}

%define pname warewulf-ipmi
%define dname ipmi
%define debug_package %{nil}
%define wwpkgdir /srv/warewulf

%if 0%{?PROJ_NAME:1}
%define rpmname %{pname}-%{PROJ_NAME}
%else
%define rpmname %{pname}
%endif

Name: %{rpmname}
Summary: IPMI Module for Warewulf
Version: 3.7
Release: %{_rel}%{?dist}
License: US Dept. of Energy (BSD-like)
Group: %{PROJ_NAME}/provisioning
URL: http://warewulf.lbl.gov/
Source0: https://github.com/crbaird/warewulf3/archive/v3.7pre.tar.gz#/warewulf3-3.7pre.tar.gz
Source1: OHPC_macros
Patch0: warewulf-ipmi-3.6-config_guess.patch
ExclusiveOS: linux
Requires: warewulf-common%{PROJ_DELIM}
BuildRequires: warewulf-common%{PROJ_DELIM}
Conflicts: warewulf < 3
BuildConflicts: post-build-checks
BuildRoot: %{?_tmppath}%{!?_tmppath:/var/tmp}/%{pname}-%{version}-%{release}-root
DocDir: %{OHPC_PUB}/doc/contrib

%description
Warewulf >= 3 is a set of utilities designed to better enable
utilization and maintenance of clusters or groups of computers.

This is the IPMI module package.  It contains Warewulf modules for
adding IPMI functionality.


%prep
%setup -n warewulf3-3.7pre
%ifarch aarch64
cd %{dname}
%patch0 -p1
%endif

%build
cd %{dname}
./autogen.sh
%configure --localstatedir=%{wwpkgdir}
%{__make} %{?mflags}


%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT %{?mflags_install}

%{__mkdir} -p $RPM_BUILD_ROOT/%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{OHPC_PUB}
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{wwpkgdir}/*
%{_libexecdir}/warewulf/ipmitool
%{perl_vendorlib}/Warewulf/Ipmi.pm
%{perl_vendorlib}/Warewulf/Module/Cli/*


%changelog
