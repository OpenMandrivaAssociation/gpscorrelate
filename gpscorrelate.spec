Name: gpscorrelate
Summary: GPS photo tagging application 
Version: 1.6.1
Release: %mkrel 4
Source0: http://freefoote.dview.net/linux/%{name}-%{version}.tar.gz
Patch0:	gpscorrelate-1.6.1-makefile.diff
URL: http://freefoote.dview.net/linux_gpscorr.html
License: GPLv2+
Group: Graphics
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: gtk+2-devel >= 2.9.0
BuildRequires: libxslt-proc
BuildRequires: docbook-style-xsl
BuildRequires: libexiv-devel

%description
This program correlates digital camera photos with GPS data in GPX format.

%prep
%setup -q
%patch0 -p1

%build
%make LDFLAGS="%{?ldflags}" CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT 

install -d $RPM_BUILD_ROOT%{_bindir}/
install  -m755 gpscorrelate gpscorrelate-gui $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc RELEASES COPYING README doc
%{_bindir}/*



%changelog
* Fri Dec 02 2011 Götz Waschk <waschk@mandriva.org> 1.6.1-4mdv2012.0
+ Revision: 737132
- fix build deps
- rebuild

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 1.6.1-3mdv2011.0
+ Revision: 604404
- rebuild for new exiv2

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 1.6.1-2mdv2011.0
+ Revision: 565540
- rebuild for new exiv2

* Thu Apr 29 2010 Funda Wang <fwang@mandriva.org> 1.6.1-1mdv2010.1
+ Revision: 540893
- New version 1.6.1

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 1.5.8-3mdv2010.1
+ Revision: 484197
- Rebuild for new libexiv2

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Jan 11 2009 Funda Wang <fwang@mandriva.org> 1.5.8-1mdv2009.1
+ Revision: 328186
- add br
- New version 1.5.8
- use flags

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.5.6-3mdv2009.0
+ Revision: 246548
- rebuild

* Mon Mar 03 2008 Frederic Crozat <fcrozat@mandriva.com> 1.5.6-1mdv2008.1
+ Revision: 177999
- import gpscorrelate


