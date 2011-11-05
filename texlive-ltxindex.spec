# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ltxindex
# catalog-date 2009-10-01 20:18:08 +0200
# catalog-license gpl
# catalog-version 0.1c
Name:		texlive-ltxindex
Version:	0.1c
Release:	1
Summary:	A LaTeX package to typeset indices with GNU's Texindex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltxindex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxindex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxindex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxindex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A LaTeX package that allows the user to make indexes with GNU's
Texindex program, instead of makeindex. It provides the
indexing commands available in Texinfo by default, but only
defines the concept index (cp) by default -- the user must
define other standard indexes, and there is no provision for
custom indexes. The package is not currently maintained.

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
%{_texmfdistdir}/tex/latex/ltxindex/ltxindex.sty
%doc %{_texmfdistdir}/doc/latex/ltxindex/README
%doc %{_texmfdistdir}/doc/latex/ltxindex/copying.txt
%doc %{_texmfdistdir}/doc/latex/ltxindex/ltxindex.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ltxindex/ltxindex.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
