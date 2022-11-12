Name:		texlive-endfloat
Version:	57090
Release:	1
Summary:	Move floats to the end, leaving markers where they belong
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/endfloat
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endfloat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endfloat.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endfloat.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/endfloat
%doc %{_texmfdistdir}/doc/latex/endfloat
#- source
%doc %{_texmfdistdir}/source/latex/endfloat

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
