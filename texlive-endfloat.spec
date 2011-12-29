# revision 24843
# category Package
# catalog-ctan /macros/latex/contrib/endfloat
# catalog-date 2011-12-13 18:42:07 +0100
# catalog-license gpl
# catalog-version 2.5b
Name:		texlive-endfloat
Version:	2.5b
Release:	2
Summary:	Move floats to the end with markers where they belong
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/endfloat
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endfloat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endfloat.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endfloat.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Place all floats on pages by themselves at the end of the
document, optionally leaving markers like "[Figure 3 about
here]" in the text near to where the figure (or table) would
normally have occurred. (Float types figure and table are
recognised by the package, unmodified. Several packages define
other types of float; it is possible to register such float
types with endfloat.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/endfloat/efxmpl.cfg
%{_texmfdistdir}/tex/latex/endfloat/endfloat.sty
%doc %{_texmfdistdir}/doc/latex/endfloat/COPYING
%doc %{_texmfdistdir}/doc/latex/endfloat/README
%doc %{_texmfdistdir}/doc/latex/endfloat/endfloat.pdf
#- source
%doc %{_texmfdistdir}/source/latex/endfloat/endfloat.dtx
%doc %{_texmfdistdir}/source/latex/endfloat/endfloat.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
