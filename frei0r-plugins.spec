%global _enable_devel_packages 1

Summary: A minimalistic plugin API for video effects
Name: frei0r-plugins
Version: 1.4
Release: 4%{?dist}
License: GPLv2+
Group: System Environment/Libraries
URL: http://frei0r.dyne.org/
Source0: https://files.dyne.org/frei0r/releases/frei0r-plugins-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: opencv-devel >= 1.0.0, gavl-devel >= 0.2.3
BuildRequires: autoconf, atrpms-rpm-config

# %{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
Frei0r is a minimalistic plugin API for video effects.

The main emphasis is on simplicity for an API that will round up the
most common video effects into simple filters, sources and mixers that
can be controlled by parameters.

%prep
%setup -q

%build
%configure --disable-static
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

 if test "%{_docdir}/%{name}" != "%{_pkgdocdir}"; then
  mkdir -p %{buildroot}%{_pkgdocdir}
  mv %{buildroot}%{_docdir}/%{name}/* %{buildroot}%{_pkgdocdir}
  rmdir %{buildroot}%{_docdir}/%{name}
 fi
# Doc files gets installed in two libraries, remove one
rm -rf %{buildroot}%{_docdir}/%{name}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO
%{_libdir}/frei0r-1

%changelog
* Wed May 6 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.4-4
- Added buildrequirement atrpms-rpm-config

* Fri May 1 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 1.4-3
- Remove one unused doc-dir when compiling on ClearOS 7
- Changed Source0 url from ftp to https since the ftp server is not responding

* Mon Mar 17 2014 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.4-2
- Update to 1.4.

* Mon Mar 14 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.3-1
- Initial build.
