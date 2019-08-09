all: main.pdf timetable.pdf abstract.pdf

main.pdf: main.tex data.csv
	latexmk -pdflatex=xelatex -pdf main.tex


timetable.pdf: timetable/timetable.tex data.csv
	cd timetable && latexmk -pdflatex=xelatex -pdf timetable.tex && mv timetable.pdf ..


abstract.pdf: abstract/abstract.tex
	cd abstract && latexmk -pdflatex=xelatex -pdf abstract.tex && mv abstract.pdf ..

clean:
	latexmk -CA
	rm abstract.pdf timetable.pdf 
