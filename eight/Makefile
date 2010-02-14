LATEX=latex
PS=dvips
PDF=ps2pdf

NAME=b_gianforcaro_hw_eight
default: pdf 

pdf: homework.tex
	$(LATEX) homework.tex
	$(PS) homework.dvi
	$(PDF) homework.ps
	mv homework.pdf $(NAME).pdf
	open $(NAME).pdf
	make clean

clean:
	rm -f homework.dvi
	rm -f homework.aux
	rm -f homework.log
	rm -f homework.pdf
	rm -f homework.toc
	rm -f homework.ps
