


abstract.pdf: abstract/abstract.tex
	cd abstract && latexmk -pdf abstract.tex && cp abstract.pdf ..
