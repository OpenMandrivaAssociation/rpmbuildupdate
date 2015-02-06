%define name	rpmbuildupdate
%define version	0.8.1
%define release 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Helps you build up to date RPMs
License:	GPL
Group:		Development/Other
URL:		http://wiki.mandriva.com/en/Development/Packaging/Tools/rpmbuildupdate
Source0:	%{name}-%{version}.tar.gz
Conflicts:	rpm-rebuilder <= 0.25-1mdk
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
rpmbuildupdate helps you build up to date RPMs. It download source tarball 
and update the spec files. It can also be used to rebuild and apply scripted
change to a spec file. 

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_sysconfdir}/bash_completion.d/%{name}
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}.conf


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.8.1-4mdv2010.0
+ Revision: 433450
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.8.1-3mdv2009.0
+ Revision: 242562
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.1-1mdv2008.0
+ Revision: 46218
- new version

* Wed May 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.0-1mdv2008.0
+ Revision: 20739
- Import rpmbuildupdate



* Wed May 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.0-1mdv2008.0
- new version

* Mon Sep 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.1-1mdv2007.0
- new version  

* Wed Jan 18 2006 Michael Scherer <misc@mandriva.org> 0.6.1-1mdk
- new release to please cvs

* Wed Jan 18 2006 Michael Scherer <misc@mandriva.org> 0.6-1mdk
- 0.6
- enhance description
- add url

* Thu Oct 06 2005 Guillaume Rousse <guillomovitch@zarb.org> 0.5-1mdk
- first individual release
