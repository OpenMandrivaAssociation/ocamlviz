%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Real-time profiling tools for Objective Caml
Name:		ocamlviz
Version:	1.01
Release:	3
License:	LGPLv2+
Group:		Development/Other
Url:		https://ocamlviz.forge.ocamlcore.org/
Source0:	http://ocamlviz.forge.ocamlcore.org/ocamlviz-%{version}.tar.gz
Source1:	META
Source2:	ocaml.xpm
BuildRequires:	camlp4
BuildRequires:	ocaml
BuildRequires:	ocaml-cairo-devel
BuildRequires:	ocaml-lablgtk2-devel
Requires:	ocaml-cairo
Requires:	ocaml-lablgtk2

%description
Ocamlviz gives the ability to instrument an existing code, in real
time, with lightweight monitoring annotations. Ocamlviz can also be
used as a debugging tool.

Here are a few possibilities provided by Ocamlviz:
 * observe details about the garbage collector
 * observe how many times the program goes through a point
 * make a set of values (any) and count its cardinal number and its
   size in the heap
 * observe how much time passed between two points of the program
 * observe the value of integers, floating-point numbers, booleans
   and strings
 * observe details about hash tables, like the number of empty
   buckets, or the filling rate
 * etc

Ocamlviz offers two sorts of client output:
 * an ASCII client, the monitoring is displayed in a file
 * a Graphical User Interface, using Lablgtk2, that allows, for
   instance, displaying data in a graph

%files
%doc LICENSE README CHANGELOG.txt
%doc docs html
%{_bindir}/ocamlviz-ascii
%{_bindir}/ocamlviz-gui
%{_libdir}/ocaml/ocamlviz/META
%{_libdir}/ocaml/ocamlviz/*.cmi
%{_libdir}/ocaml/ocamlviz/*.mli
%{_libdir}/ocaml/ocamlviz/*.cma
%{_libdir}/ocaml/ocamlviz/*.cmxa
%{_libdir}/ocaml/ocamlviz/*.a
%{_libdir}/ocaml/ocamlviz/camlp4/*
%{_mandir}/man1/ocamlviz.1*
%{_datadir}/pixmaps/ocaml.xpm

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}
cp %{SOURCE1} META
sed -i -e "s:@VERSION@:%{version}:g" META
cp %{SOURCE2} .

%build
./configure
make

%install
install -d %{buildroot}/`ocamlc -where`/ocamlviz
install -d %{buildroot}/`ocamlc -where`/ocamlviz/camlp4
install -d %{buildroot}%{_datadir}/pixmaps/
make install prefix=%{buildroot}%{_prefix} OCAMLLIB=%{buildroot}/`ocamlc -where`/ocamlviz
install -m 0644 camlp4/pa_ocamlviz.ml %{buildroot}/`ocamlc -where`/ocamlviz/camlp4/
install -m 0644 META %{buildroot}/`ocamlc -where`/ocamlviz/
install -m 0644 ocaml.xpm %{buildroot}%{_datadir}/pixmaps/

mv doc docs
mkdir doc
make doc
mv doc html

