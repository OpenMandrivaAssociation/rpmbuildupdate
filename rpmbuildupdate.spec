%define name	rpmbuildupdate
%define version	0.8.1
%define release %mkrel 1

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
