LATEX=pdflatex
CONVERT_DVI=dvipdf
NAME=b_gianforcaro_hw_three
default: pdf 

pdf: homework.tex
	$(LATEX) homework.tex
	rm -rf homework.log
	rm -rf homework.aux
	mv homework.pdf $(NAME).pdf
	open $(NAME).pdf 

clean:
	rm -f homework.dvi
	rm -f homework.aux
	rm -f homework.log
	rm -f homework.pdf
	rm -f homework.toc
