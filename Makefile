
main.pdf: main.tex
	latexmk -pdflatex=xelatex -pdf main.tex


timetable.pdf: timetable/timetable.tex
	cd timetable && latexmk -pdflatex=xelatex -pdf timetable.tex && cp timetable.pdf ..


abstract.pdf: abstract/abstract.tex
	cd abstract && latexmk -pdflatex=xelatex -pdf abstract.tex && cp abstract.pdf ..

clean:
	latexmk -CA
