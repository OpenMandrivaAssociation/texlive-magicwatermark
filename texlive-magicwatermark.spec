Name:		texlive-magicwatermark
Version:	63656
Release:	2
Summary:	An easy and flexible way to set watermarks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/magicwatermark
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magicwatermark.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magicwatermark.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magicwatermark.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can flexibly set and clear watermarks. It is based
on everypage and TikZ, encapsulated by LaTeX3. All watermark
content is placed inside a TikZ node in the center of the page.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/magicwatermark
%{_texmfdistdir}/tex/latex/magicwatermark
%doc %{_texmfdistdir}/doc/latex/magicwatermark

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
