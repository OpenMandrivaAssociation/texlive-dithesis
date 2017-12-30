# revision 34295
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-dithesis
Version:	0.2
Release:	1
Summary:	TeXLive dithesis package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dithesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dithesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive dithesis package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dithesis/dithesis.cls
%doc %{_texmfdistdir}/doc/latex/dithesis/README
%doc %{_texmfdistdir}/doc/latex/dithesis/athena.jpg
%doc %{_texmfdistdir}/doc/latex/dithesis/sample.pdf
%doc %{_texmfdistdir}/doc/latex/dithesis/sample.tex
%doc %{_texmfdistdir}/doc/latex/dithesis/sampleNoArial.pdf
%doc %{_texmfdistdir}/doc/latex/dithesis/sampleNoArial.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
