% Beamer coderdojoka documentclass

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{coderdojokabeamer}[2015/04/26 v. 1.0 Coderdojo Karlsruhe documentclass for presentations]

\LoadClass[xcolor=svgnames]{beamer}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}

\usepackage[ngerman]{babel}

\usepackage{csquotes}
\MakeOuterQuote{"}

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

% \usepackage instead of \usetheme to support relative paths
\usepackage{\VorlagenPfad/beamerthemecoderdojoka}