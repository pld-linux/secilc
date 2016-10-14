#
# Conditional build:
%bcond_without	doc	# HTML documentation
#
%ifnarch %{ix86} %{x8664}
# pandoc requires ghc
%undefine	with_doc
%endif
Summary:	SELinux Common Intermediate Language (CIL) Compiler
Summary(pl.UTF-8):	Kompilator języka pośredniego (CIL) SELinuksa
Name:		secilc
Version:	2.5
Release:	2
License:	BSD
Group:		Applications
#Source0Download: https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:	https://raw.githubusercontent.com/wiki/SELinuxProject/selinux/files/releases/20160223/%{name}-%{version}.tar.gz
# Source0-md5:	af73267cccd0e46cb455d5702565cd41
URL:		https://github.com/SELinuxProject/cil/wiki
BuildRequires:	gcc >= 6:4.5.1
BuildRequires:	libsepol-devel >= 2.5
%{?with_doc:BuildRequires:	pandoc}
BuildRequires:	xmlto
Requires:	libsepol >= 2.5
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
%doc COPYING ChangeLog README %{?with_doc:docs/html}
%attr(755,root,root) %{_bindir}/secilc
%{_mandir}/man8/secilc.8*
