\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{refdoc}[2018/12/28 Reference Documentation class]

\newcommand{\headlinecolor}{\normalcolor}
\LoadClass{article}

\usepackage{minted}
\usepackage{graphicx}
\usepackage{scrextend}
\usepackage[pdf]{graphviz}

\newcommand{\lsec}[1]{}
\let\lsec=\section
\renewcommand{\section}[1]{\lsec{#1}\noindent\rule{\textwidth}{2pt}\vspace{10pt}}

\newcommand{\lssec}[1]{}
\let\lssec=\subsection
\renewcommand{\subsection}[1]{\lssec{#1}\noindent\rule{\textwidth}{1pt}\vspace{5pt}}

\newcommand{\lsssec}[1]{}
\let\lsssec=\subsubsection
\renewcommand{\subsubsection}[1]{\lsssec{#1}\noindent\rule{\textwidth}{0.5pt}\vspace{2.5pt}}

\newcounter{function}[section]
\newenvironment{func}[1]
{\refstepcounter{function}\vspace{5pt}\normalfont\large\bfseries#1()\normalfont\normalsize
\begin{addmargin}{1em}
\noindent\rule{\textwidth}{1pt}\newline}
{\end{addmargin}}

\newcounter{enum}[section]
\newenvironment{enum}[1]
{\refstepcounter{enum}\vspace{5pt}\normalfont\large\bfseries#1\normalfont\normalsize
\begin{addmargin}{1em}
\noindent\rule{\textwidth}{1pt}\newline}
{\end{addmargin}}

\newcounter{struct}[section]
\newenvironment{struct}[1]
{\refstepcounter{struct}\vspace{5pt}\normalfont\large\bfseries#1\normalfont\normalsize
\begin{addmargin}{1em}
\noindent\rule{\textwidth}{1pt}\newline}
{\end{addmargin}}

\newenvironment{nitem}[1]
{\normalfont\normalsize\bfseries #1\normalfont\normalsize\begin{itemize}}
{\end{itemize}}

\newenvironment{params}{\begin{nitem}{Parameters}}{\end{nitem}}
\newenvironment{enumerator}{\begin{nitem}{Enumerator}}{\end{nitem}}
\newenvironment{data}{\begin{nitem}{Data Fields}}{\end{nitem}}

\newcommand{\src}[1]{\mintinline{c}{#1}\newline}
\newcommand{\param}[3][]{\item[] \mintinline{c}{#2} \textit{\textbf{#1}} #3}
\newcommand{\val}[2]{\item[] \mintinline{c}{#1} #2}
\newcommand{\field}[3]{\item[] \mintinline{c}{#1} \mintinline{c}{#2} #3}
\newcommand{\return}[1]{\begin{nitem}{Returns}\item[] #1\end{nitem}}
