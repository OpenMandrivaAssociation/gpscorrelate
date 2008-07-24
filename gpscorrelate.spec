Name: gpscorrelate
Summary: GPS photo tagging application 
Version: 1.5.6
Release: %mkrel 3
Source0:	http://freefoote.dview.net/linux/%{name}-%{version}.tar.gz
URL:		http://freefoote.dview.net/linux_gpscorr.html
License:	GPLv2+
Group:		Graphics
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:  gtk+2-devel >= 2.9.0
BuildRequires:  libexiv-devel

%description
This program correlates digital camera photos with GPS data in GPX format.

%prep
%setup -q

%build

%make
										
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

