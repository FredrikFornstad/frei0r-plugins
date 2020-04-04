%global _enable_devel_packages 1

Summary: A minimalistic plugin API for video effects
Name: frei0r-plugins
Version: 1.7.0
Release: 1%{?dist}
License: GPLv2+
Group: System Environment/Libraries
URL: http://frei0r.dyne.org/
Source0: https://files.dyne.org/frei0r/releases/frei0r-plugins-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: opencv-devel >= 1.0.0, gavl-devel >= 0.2.3
BuildRequires: autoconf, libtool

%description
Frei0r is a minimalistic plugin API for video effects.

The main emphasis is on simplicity for an API that will round up the
most common video effects into simple filters, sources and mixers that
can be controlled by parameters.

%package devel
Summary: frei0r-plugins development files.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package contains the frei0r-plugins development files.

%prep
%setup -q

%build
mkdir -p m4
autoreconf -i
%configure --disable-static
# frei0r makefile expecting other file names
mv README.txt README.md
mv ChangeLog.txt ChangeLog
mv TODO.txt TODO
mv AUTHORS.txt AUTHORS
make %(?_smp_mflags)

%install
# rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

# Doc files gets installed in two libraries, remove one
rm -rf %{buildroot}%{_docdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING.txt ChangeLog README.md TODO
%{_libdir}/frei0r-1

%files devel
%defattr(-,root,root,-)
%{_includedir}/frei0r.h
%{_libdir}/pkgconfig/frei0r.pc

%changelog
* Sat Apr 4 2020 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.7.0-1
- New upstream release

* Mon Jun 5 2017 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.6.1-1
- New upstream release
- Added .txt back to some files to adjust for upstream build changes

* Sat Apr 8 2017 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.6.0-1
- New upstream release
- Modified spec file

* Sun Aug 21 2016 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.0-2
- removed .txt from some file names and adding Makefile.in files to adjust for new upstream packaging

* Sat Aug 20 2016 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.5.0-1
- New upstream release

* Sat Jun 13 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.4-4
- Removed dependency on atrpms rpm scripts to comply with ClearOS policy

* Fri May 1 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.4-3
- Remove one unused doc-dir when compiling on ClearOS 7
- Changed Source0 url from ftp to https since the ftp server is not responding

* Mon Mar 17 2014 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.4-2
- Update to 1.4.

* Mon Mar 14 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.3-1
- Initial build.
