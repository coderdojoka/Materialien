% Text coderdojoka documentclass

%\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{coderdojokatext}[2015/04/26 v. 1.0 Coderdojo Karlsruhe documentclass for text]

\LoadClass[xcolor=svgnames, oneside, a4letter]{scrbook}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[ngerman]{babel}

\usepackage{fancyhdr} % Required for custom headers
\usepackage{lastpage} % Required to determine the last page for the footer
\usepackage{extramarks} % Required for headers and footers
\usepackage{graphicx}
\usepackage{courier} % Required for the courier font
\usepackage[many]{tcolorbox}

% Autor für die Kopfzeile
\newcommand{\Autor}{CoderDojo Karlsruhe}

% Header Konfiguration
\pagestyle{fancy}
\setcounter{chapter}{1}

%\chead{\Titel} % Top center head
\rhead{\Autor} % Top left header
%\rfoot{Seite\ \thepage\ von\ \protect\pageref{LastPage}} % Bottom right footer
\renewcommand\headrulewidth{0.4pt} % Size of the header rule
\renewcommand\footrulewidth{0.4pt} % Size of the footer rule

\setlength\parindent{0pt} % Removes all indentation from paragraphs


\usepackage{csquotes}

\usepackage{minted}
%Prior to version 2.0 minted cannot handle non-english characters
%we apply a workaround if we detect an earlier version
\@ifpackagelater{minted}{2015/01/31}
{
	%Package is new enough
}
{
	\newcommand{\minted@write@detok}[1]{%
	  \immediate\write\FV@OutFile{\detokenize{#1}}}%
	
	\newcommand{\minted@FVB@VerbatimOut}[1]{%
	  \@bsphack
	  \begingroup
	    \FV@UseKeyValues
	    \FV@DefineWhiteSpace
	    \def\FV@Space{\space}%
	    \FV@DefineTabOut
	    %\def\FV@ProcessLine{\immediate\write\FV@OutFile}% %Old, non-Unicode version
	    \let\FV@ProcessLine\minted@write@detok %Patch for Unicode
	    \immediate\openout\FV@OutFile #1\relax
	    \let\FV@FontScanPrep\relax
	%% DG/SR modification begin - May. 18, 1998 (to avoid problems with ligatures)
	    \let\@noligs\relax
	%% DG/SR modification end
	    \FV@Scan}
	    \let\FVB@VerbatimOut\minted@FVB@VerbatimOut
	
	\renewcommand\minted@savecode[1]{
	  \immediate\openout\minted@code\jobname.pyg
	  \immediate\write\minted@code{\expandafter\detokenize\expandafter{#1}}%
	  \immediate\closeout\minted@code}
}

\newcommand{\code}[1]{
	\begin{ttfamily}#1\end{ttfamily}
}

\newminted{python}{linenos, stepnumber=1, tabsize=4}
\newminted[pseudocode]{php}{linenos, stepnumber=1, tabsize=4}

\newtcolorbox{merkbox}[1][]{
  breakable,
  freelance,
  title=#1,
  before=\par\bigskip,
  after=\par\bigskip,
  colback=white,
  colbacktitle=white,
  coltitle=black,
  fonttitle=\bfseries,
  bottomrule=0pt,
  boxrule=0pt,
  colframe=white,
  overlay unbroken and first={
  \draw[red!75!black,line width=3pt]
    ([xshift=5pt]frame.north west) -- 
    (frame.north west) -- 
    (frame.south west);
  \draw[red!75!black,line width=3pt]
    ([xshift=-5pt]frame.north east) -- 
    (frame.north east) -- 
    (frame.south east);
  },
  overlay unbroken app={
  \draw[red!75!black,line width=3pt,line cap=rect]
    (frame.south west) -- 
    ([xshift=5pt]frame.south west);
  \draw[red!75!black,line width=3pt,line cap=rect]
    (frame.south east) -- 
    ([xshift=-5pt]frame.south east);
  },
  overlay middle and last={
  \draw[red!75!black,line width=3pt]
    (frame.north west) -- 
    (frame.south west);
  \draw[red!75!black,line width=3pt]
    (frame.north east) -- 
    (frame.south east);
  },
  overlay last app={
  \draw[red!75!black,line width=3pt,line cap=rect]
    (frame.south west) --
    ([xshift=5pt]frame.south west);
  \draw[red!75!black,line width=3pt,line cap=rect]
    (frame.south east) --
    ([xshift=-5pt]frame.south east);
  },
}
