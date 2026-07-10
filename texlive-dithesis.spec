%global tl_name dithesis
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	A class for undergraduate theses at the University of Athens
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dithesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dithesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dithesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class conforms to the requirements of the Department of Informatics
and Telecommunications at the University of Athens regarding the
preparation of undergraduate theses, as of Sep 1, 2011. The class is
designed for use with XeLaTeX; by default (on a Windows platform), the
font Arial is used, but provision is made for use under Linux (with a
different sans-serif font).

