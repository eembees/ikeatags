import csv

preamble = open("preamble.tex", "r").read()

template = r"""\fbox{
\begin{minipage}[t][15cm]{5cm}
\makebox[\linewidth][l]{\large %(top_text)s\strut}  
\vspace{1cm}
\makebox[\linewidth][l]{\huge\textbf{\textsc{%(title)s}}}
\vspace{0.5cm}
\parbox[\linewidth]{\large %(sub_title)s\hfill}
\raggedleft
\begin{itemize}
  \item \textbf{%(item_1)s}
  \item \textbf{%(item_2)s}
  \item \textbf{%(item_3)s}
  \item \textbf{%(item_4)s}
\end{itemize}
\vfill
\makebox[\linewidth]{Design:\hspace{1cm}\hfill %(designer)s}
\resizebox{!}{1.2cm}{\textbf{%(price)s}\hfill}
\makebox[\linewidth]{\Huge{\textbf{%(valuta)s}}\hfill}
\end{minipage}}
"""
page = ""
with open('in.csv',newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        page += template %  row


with open("out.tex", "w") as f:
    f.write(preamble)
    f.write("\\begin{document}")
    f.write("\\pagenumbering{gobble}")
    f.write(page)
    f.write("\\end{document}")