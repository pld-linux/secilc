#
# Conditional build:
%bcond_without	doc	# HTML documentation
#
%define	selinux_ver	3.8
Summary:	SELinux Common Intermediate Language (CIL) Compiler
Summary(pl.UTF-8):	Kompilator języka pośredniego (CIL) SELinuksa
Name:		secilc
Version:	3.8
Release:	1
License:	BSD
Group:		Applications
#Source0Download: https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:	https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0c35dca01cd001c8711edcccc9a8ae01
URL:		https://github.com/SELinuxProject/cil/wiki
BuildRequires:	gcc >= 6:4.5.1
BuildRequires:	libsepol-devel >= %{selinux_ver}
%{?with_doc:BuildRequires:	pandoc >= 2.0}
BuildRequires:	xmlto
Requires:	libsepol >= %{selinux_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SELinux CIL Compiler is a compiler that converts the CIL language
as described on the CIL design wiki into a kernel binary policy file.

%description -l pl.UTF-8
SELinux CIL Compiler to kompilator przekształcający język CIL (Common
Intermediate Language - wspólny język pośredni), zgodny z opisem na
stronie wiki, do postaci binarnego pliku polityki jądra.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
CPPFLAGS="%{rpmcppflags}" \
%{__make} \
	CC="%{__cc}" \
	LIBDIR=%{_libdir}

%if %{with doc}
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README %{?with_doc:docs/html}
%attr(755,root,root) %{_bindir}/secil2conf
%attr(755,root,root) %{_bindir}/secil2tree
%attr(755,root,root) %{_bindir}/secilc
%{_mandir}/man8/secil2conf.8*
%{_mandir}/man8/secil2tree.8*
%{_mandir}/man8/secilc.8*
