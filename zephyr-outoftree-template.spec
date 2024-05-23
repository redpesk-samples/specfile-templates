%global debug_package %{nil}
%define __strip /bin/true

%define targetname     _TO_COMPLETE_
%define firmwarename   _TO_COMPLETE_
%define filename       zephyr-%{firmwarename}-%{targetname}

Name: _TO_COMPLETE_
#Hexsha: 3c4ce801fdf6d7fe8babf3c3cf0255c5a57a646a
Version: _TO_COMPLETE_
Release: 0%{?dist}
Summary: _TO_COMPLETE_

License: _TO_COMPLETE_
URL: _TO_COMPLETE_
Source0: %{name}-%{version}.tar.gz

#Main Zephyr require
BuildRequires: zephyr-kernel
BuildRequires: zephyr-kernel-modules-common
#Needed Zephyr toolchain
BuildRequires: zephyr-toolchain-_TO_COMPLETE_

%description
_TO_COMPLETE_

%prep
%autosetup

%build
%{westbuild} -b %{targetname} .

%install
%{__install} -d %{buildroot}/lib/firmware
%{__install} -m 755 build/zephyr/zephyr.bin %{buildroot}/lib/firmware/%{filename}.bin
%{__install} -m 755 build/zephyr/zephyr.elf %{buildroot}/lib/firmware/%{filename}.elf

%files
/lib/firmware

%changelog
