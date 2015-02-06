Summary:	Dhcp daemon ping program
Name:           dhcping
Version:        1.2
Release:        14
License:        BSD
Group:		Networking/Other
URL:		http://www.mavetju.org/unix/general.php
Source:         http://www.mavetju.org/download/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This small tool let you perform a dhcp-request to find out if a dhcp-server is
still running.

%prep

%setup -q

%build

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CONTACT
%{_bindir}/*
%{_mandir}/*/*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2-13mdv2011.0
+ Revision: 617579
- the mass rebuild of 2010.0 packages

* Sun Oct 04 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2-12mdv2010.0
+ Revision: 453454
- rebuild
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 8mdv2008.1-current
+ Revision: 136362
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org> 1.2-8mdv2007.0
+ Revision: 53245
- rebuild
- Import dhcping

* Tue Dec 20 2005 Olivier Thauvin <nanardon@mandriva.org> 1.3-7mdk
- %%mkrel
- rebuild

* Mon Nov 29 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2-6mdk
- make it rpmbuildupdate aware

* Mon May 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2-5mdk
- use macros

