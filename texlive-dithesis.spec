Name:		texlive-dithesis
Version:	34295
Release:	1
Summary:	TeXLive dithesis package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dithesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dithesis.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
