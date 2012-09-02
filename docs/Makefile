tex:
	pandoc ../README.md -o README.1.tex
	cat latex_header README.1.tex latex_footer > README.tex
	sed -i s/verbatim/lstlisting/ README.tex
	sed -i s/subsection{/subsection*{/ README.tex
	sed -i s/section{/section*{/ README.tex
clean:
	rm README.1.tex README.tex README.log README.aux