# revision 24962
# category Package
# catalog-ctan /macros/latex/contrib/endfloat
# catalog-date 2011-12-24 01:13:38 +0100
# catalog-license gpl
# catalog-version 2.5c
Name:		texlive-endfloat
Version:	2.5c
Release:	8
Summary:	Move floats to the end, leaving markers where they belong
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
normally have occurred. Float types figure and table are
recognised by the package, unmodified. Since several packages
define other types of float, it is possible to register these
float types with endfloat.

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


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.5c-1
+ Revision: 758862
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.5b-3
+ Revision: 751417
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.5b-2
+ Revision: 745210
- texlive-endfloat

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.5b-1
+ Revision: 743252
- texlive-endfloat

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.4i-1
+ Revision: 718331
- texlive-endfloat
- texlive-endfloat
- texlive-endfloat
- texlive-endfloat

