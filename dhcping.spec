%define name	dhcping
%define version	1.2
%define release %mkrel 10

Summary:	Dhcp daemon ping program
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        BSD
Group:		Networking/Other
URL:		http://www.mavetju.org/unix/general.php
Source:         http://www.mavetju.org/download/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
This small tool let you perform a dhcp-request to find out
if a dhcp-server is still running.

%prep

%setup -q

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CONTACT
%{_bindir}/*
%{_mandir}/*/*


