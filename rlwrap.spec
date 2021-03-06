#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rlwrap
Version  : 0.45.2
Release  : 5
URL      : https://github.com/hanslub42/rlwrap/archive/v0.45.2/rlwrap-0.45.2.tar.gz
Source0  : https://github.com/hanslub42/rlwrap/archive/v0.45.2/rlwrap-0.45.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: rlwrap-bin = %{version}-%{release}
Requires: rlwrap-data = %{version}-%{release}
Requires: rlwrap-license = %{version}-%{release}
Requires: rlwrap-man = %{version}-%{release}
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(ncurses)
BuildRequires : readline-dev

%description
The filters in this directory have been written to test rlwrap,
not to be practical.

%package bin
Summary: bin components for the rlwrap package.
Group: Binaries
Requires: rlwrap-data = %{version}-%{release}
Requires: rlwrap-license = %{version}-%{release}

%description bin
bin components for the rlwrap package.


%package data
Summary: data components for the rlwrap package.
Group: Data

%description data
data components for the rlwrap package.


%package dev
Summary: dev components for the rlwrap package.
Group: Development
Requires: rlwrap-bin = %{version}-%{release}
Requires: rlwrap-data = %{version}-%{release}
Provides: rlwrap-devel = %{version}-%{release}
Requires: rlwrap = %{version}-%{release}

%description dev
dev components for the rlwrap package.


%package license
Summary: license components for the rlwrap package.
Group: Default

%description license
license components for the rlwrap package.


%package man
Summary: man components for the rlwrap package.
Group: Default

%description man
man components for the rlwrap package.


%prep
%setup -q -n rlwrap-0.45.2
cd %{_builddir}/rlwrap-0.45.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623775705
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1623775705
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rlwrap
cp %{_builddir}/rlwrap-0.45.2/COPYING %{buildroot}/usr/share/package-licenses/rlwrap/dfac199a7539a404407098a2541b9482279f690d
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rlwrap

%files data
%defattr(-,root,root,-)
/usr/share/rlwrap/completions/coqtop
/usr/share/rlwrap/completions/testclient
/usr/share/rlwrap/filters/README
/usr/share/rlwrap/filters/RlwrapFilter.3pm
/usr/share/rlwrap/filters/RlwrapFilter.pm
/usr/share/rlwrap/filters/censor_passwords
/usr/share/rlwrap/filters/censor_passwords.py
/usr/share/rlwrap/filters/count_in_prompt
/usr/share/rlwrap/filters/count_in_prompt.py
/usr/share/rlwrap/filters/debug_null
/usr/share/rlwrap/filters/dissect_prompt
/usr/share/rlwrap/filters/edit_history
/usr/share/rlwrap/filters/ftp_filter
/usr/share/rlwrap/filters/ftp_filter.py
/usr/share/rlwrap/filters/handle_hotkeys
/usr/share/rlwrap/filters/handle_hotkeys.py
/usr/share/rlwrap/filters/handle_sigwinch
/usr/share/rlwrap/filters/history_format
/usr/share/rlwrap/filters/listing
/usr/share/rlwrap/filters/logger
/usr/share/rlwrap/filters/logger.py
/usr/share/rlwrap/filters/makefilter
/usr/share/rlwrap/filters/null
/usr/share/rlwrap/filters/null.py
/usr/share/rlwrap/filters/outfilter
/usr/share/rlwrap/filters/paint_prompt
/usr/share/rlwrap/filters/paint_prompt.py
/usr/share/rlwrap/filters/pipeline
/usr/share/rlwrap/filters/pipeto
/usr/share/rlwrap/filters/pipeto.py
/usr/share/rlwrap/filters/rlwrapfilter.py
/usr/share/rlwrap/filters/scrub_prompt
/usr/share/rlwrap/filters/simple_macro
/usr/share/rlwrap/filters/template
/usr/share/rlwrap/filters/unbackspace

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/RlwrapFilter.3pm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rlwrap/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/rlwrap.1
