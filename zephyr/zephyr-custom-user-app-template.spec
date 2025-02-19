%global debug_package %{nil}
%define __strip /bin/true

%define targetname      _TO_COMPLETE_
%define targettoolchain _TO_COMPLETE_
%define firmwarename    _TO_COMPLETE_
%define filename        zephyr-%{firmwarename}-%{targetname}

Name: _TO_COMPLETE_
Version: _TO_COMPLETE_
Release: 0%{?dist}
Summary: _TO_COMPLETE_

License: _TO_COMPLETE_
URL: _TO_COMPLETE_
Source0: %{name}-%{version}.tar.gz

# Required Zephyr packages
BuildRequires: zephyr-kernel
BuildRequires: zephyr-toolchain-%{targettoolchain}
%if "%{targetname}" != "qemu_x86_64"
BuildRequires: zephyr-kernel-hal
%endif

%description
_TO_COMPLETE_

%prep
%autosetup

%build
%{westbuild} -b %{targetname} .
%if "%{targetname}" == "qemu_x86_64"
cd build && ninja qemu_locore_image_target qemu_main_image_target
%endif

%install
%{__install} -d %{buildroot}/lib/firmware
%{__install} -m 755 build/zephyr/zephyr.elf %{buildroot}/lib/firmware/%{filename}.elf | true
%{__install} -m 755 build/zephyr/zephyr.bin %{buildroot}/lib/firmware/%{filename}.bin | true
%{__install} -m 755 build/zephyr/zephyr.hex %{buildroot}/lib/firmware/%{filename}.hex | true
%if "%{targetname}" == "qemu_x86_64"
%{__install} -m 755 build/zephyr/zephyr*qemu*.elf %{buildroot}/lib/firmware/ | true
%endif

%files
/lib/firmware

%changelog
