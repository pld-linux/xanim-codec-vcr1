Summary:	ATI VCR1 codec for XAnim
Summary(pl.UTF-8):   Kodek ATI VCR1 dla XAnima
Name:		xanim-codec-vcr1
Version:	1.0
Release:	1
License:	unknown
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/vid_vcr1_1.0_linuxELFx86c6.xa.gz
# NoSource0-md5:	77f949dc4b0dc03e35575827c580ba4d
NoSource:	0
Requires:	xanim >= 1:2920
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ATI VCR1 codec decompression DLL for XAnim.

%description -l pl.UTF-8
Biblioteka do dekompresji kodeka ATI VCR1 dla XAnima.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/xanim

gzip -dc %{SOURCE0} > $RPM_BUILD_ROOT%{_libdir}/xanim/vid_vcr1_1.0_linuxELFx86c6.xa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xanim/vid_vcr1_*.xa
