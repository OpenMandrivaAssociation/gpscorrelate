Summary:	GPS photo tagging application
Name:		gpscorrelate
Version:	2.0
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		https://dfandrich.github.io/gpscorrelate/
Source0:	https://github.com/dfandrich/gpscorrelate/releases/download/%{version}/gpscorrelate-%{version}.tar.xz
Patch0:		gpscorrelate-2.0-exiv2-0.28.patch
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
This program correlates digital camera photos with GPS data in GPX format.

%files
%{_bindir}/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%make_build LDFLAGS="%{ldflags}" CFLAGS="%{optflags}"

%install
install -d %{buildroot}%{_bindir}
install -m 755 gpscorrelate gpscorrelate-gui %{buildroot}%{_bindir}
