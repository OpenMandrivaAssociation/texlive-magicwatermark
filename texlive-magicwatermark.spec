%global tl_name magicwatermark
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2B
Release:	%{tl_revision}.1
Summary:	An easy and flexible way to set watermarks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/magicwatermark
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/magicwatermark.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/magicwatermark.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package can flexibly set and clear watermarks. It is based on
everypage and TikZ, encapsulated by LaTeX3. All watermark content is
placed inside a TikZ node in the center of the page.

