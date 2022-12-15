#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openpace
Version  : 1cc39101b14537a0da515eb1843b6fef74ccc8b5
Release  : 1
URL      : https://github.com/frankmorgner/openpace/archive/1cc39101b14537a0da515eb1843b6fef74ccc8b5/openpace-1cc39101b14537a0da515eb1843b6fef74ccc8b5.tar.gz
Source0  : https://github.com/frankmorgner/openpace/archive/1cc39101b14537a0da515eb1843b6fef74ccc8b5/openpace-1cc39101b14537a0da515eb1843b6fef74ccc8b5.tar.gz
Summary  : @PACKAGE_SUMMARY@
Group    : Development/Tools
License  : GPL-3.0
Requires: openpace-bin = %{version}-%{release}
Requires: openpace-lib = %{version}-%{release}
Requires: openpace-license = %{version}-%{release}
Requires: openpace-man = %{version}-%{release}
BuildRequires : buildreq-golang
BuildRequires : gengetopt-bin
BuildRequires : help2man
BuildRequires : pkgconfig(libcrypto)
BuildRequires : sed

%description
# OpenPACE *- Cryptographic library for EAC version 2*
OpenPACE implements Extended Access Control (EAC) version 2 as specified in
BSI TR-03110. OpenPACE comprises support for the following protocols:

%package bin
Summary: bin components for the openpace package.
Group: Binaries
Requires: openpace-license = %{version}-%{release}

%description bin
bin components for the openpace package.


%package dev
Summary: dev components for the openpace package.
Group: Development
Requires: openpace-lib = %{version}-%{release}
Requires: openpace-bin = %{version}-%{release}
Provides: openpace-devel = %{version}-%{release}
Requires: openpace = %{version}-%{release}

%description dev
dev components for the openpace package.


%package doc
Summary: doc components for the openpace package.
Group: Documentation
Requires: openpace-man = %{version}-%{release}

%description doc
doc components for the openpace package.


%package lib
Summary: lib components for the openpace package.
Group: Libraries
Requires: openpace-license = %{version}-%{release}

%description lib
lib components for the openpace package.


%package license
Summary: license components for the openpace package.
Group: Default

%description license
license components for the openpace package.


%package man
Summary: man components for the openpace package.
Group: Default

%description man
man components for the openpace package.


%prep
%setup -q -n openpace-1cc39101b14537a0da515eb1843b6fef74ccc8b5
cd %{_builddir}/openpace-1cc39101b14537a0da515eb1843b6fef74ccc8b5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671064536
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%reconfigure --disable-static
make

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check

%install
export SOURCE_DATE_EPOCH=1671064536
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openpace
cp %{_builddir}/openpace-%{version}/COPYING %{buildroot}/usr/share/package-licenses/openpace/8f5ba548fe758a98a88857c90611089a657b786d
%make_install
## install_append content
find %{buildroot} -type f -name .nojekyll -exec rm {} +
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cvc-create
/usr/bin/cvc-print
/usr/bin/eactest
/usr/bin/example

%files dev
%defattr(-,root,root,-)
/usr/include/eac/ca.h
/usr/include/eac/cv_cert.h
/usr/include/eac/eac.h
/usr/include/eac/objects.h
/usr/include/eac/pace.h
/usr/include/eac/ri.h
/usr/include/eac/ta.h
/usr/lib64/libeac.so
/usr/lib64/pkgconfig/libeac.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/openpace/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libeac.so.3
/usr/lib64/libeac.so.3.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openpace/8f5ba548fe758a98a88857c90611089a657b786d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cvc-create.1
/usr/share/man/man1/cvc-print.1
