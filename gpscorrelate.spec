Summary:	GPS photo tagging application
Name:		gpscorrelate
Version:	1.6.1
Release:	5
License:	GPLv2+
Group:		Graphics
Url:		http://freefoote.dview.net/linux_gpscorr.html
Source0:	http://freefoote.dview.net/linux/%{name}-%{version}.tar.gz
Patch0:		gpscorrelate-1.6.1-makefile.diff
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
This program correlates digital camera photos with GPS data in GPX format.

%files
%doc RELEASES COPYING README doc
%{_bindir}/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%make LDFLAGS="%{ldflags}" CFLAGS="%{optflags}"

%install
install -d %{buildroot}%{_bindir}
install -m 755 gpscorrelate gpscorrelate-gui %{buildroot}%{_bindir}


