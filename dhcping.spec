Summary:	Dhcp daemon ping program
Name:           dhcping
Version:        1.2
Release:        %mkrel 13
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
