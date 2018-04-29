Summary:	Brushes to be used with the MyPaint library
Name:		mypaint-brushes
Version:	1.3.0
Release:	1
# According to Licenses.dep5 the files used for building/installing are GPLv2+
# but the shipped brush files are CC0
License:	CC0
Group:		Applications/Graphics
URL:		https://github.com/Jehan/mypaint-brushes
Source0:	https://github.com/Jehan/mypaint-brushes/archive/v%{version}.tar.gz
# Source0-md5:	679190d88f67a94db57ac99017f966f5
BuildRequires:	autoconf
BuildRequires:	automake
BuildArch:	noarch

%package devel
Summary:	Files for developing with mypaint-brushes

%description
This package contains brush files for use with MyPaint and other
programs.

%description devel
This package contains a pkgconfig file which makes it easier to
develop programs using these brush files.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%doc COPYING Licenses.dep5 Licenses.md
%dir %{_datadir}/mypaint-data
%dir %{_datadir}/mypaint-data/*.*
%{_datadir}/mypaint-data/*.*/brushes

%files devel
%defattr(644,root,root,755)
%doc COPYING Licenses.dep5 Licenses.md
%{_npkgconfigdir}/mypaint-brushes-*.*.pc
