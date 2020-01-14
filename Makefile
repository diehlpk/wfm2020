all: main.pdf timetable.pdf abstract.pdf

main.pdf: main.tex data.csv abstract/content.tex
	latexmk -pdf main.tex


timetable.pdf: timetable/timetable.tex data.csv timetable/content.tex
	cd timetable && latexmk -pdflatex=xelatex -pdf timetable.tex && mv timetable.pdf ..


abstract.pdf: abstract/abstract.tex abstract/content.tex
	cd abstract && latexmk -pdflatex=xelatex -pdf abstract.tex && mv abstract.pdf ..

clean:
	latexmk -pdf -CA
	cd abstract && latexmk -pdf  -CA
	cd timetable && latexmk -pdf -CA

images:
	convert -density 900 -background white -alpha remove -alpha off timetable.pdf timetable.png
