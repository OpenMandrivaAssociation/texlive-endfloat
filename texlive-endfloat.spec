Name:		texlive-endfloat
Version:	2.4i
Release:	1
Summary:	Move floats to the end with markers where they belong
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/endfloat
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endfloat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endfloat.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endfloat.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Place all figures on pages by themselves at the end of the
document, optionally leaving markers like "[Figure 3 about
here]" in the text near to where the figure (or table) would
normally have occurred. (The current maintainer has announced
that he would like to relinquish control of the package;
potential maintainers are solicited...).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/endfloat/efxmpl.cfg
%{_texmfdistdir}/tex/latex/endfloat/endfloat.sty
%doc %{_texmfdistdir}/doc/latex/endfloat/COPYING
%doc %{_texmfdistdir}/doc/latex/endfloat/endfloat.asc
%doc %{_texmfdistdir}/doc/latex/endfloat/endfloat.pdf
%doc %{_texmfdistdir}/doc/latex/endfloat/readme.enf
#- source
%doc %{_texmfdistdir}/source/latex/endfloat/endfloat.drv
%doc %{_texmfdistdir}/source/latex/endfloat/endfloat.dtx
%doc %{_texmfdistdir}/source/latex/endfloat/endfloat.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
