MAIN := main
PDF := $(MAIN).pdf
LATEXMK := latexmk

LATEX_ARTIFACTS := \
	*.acn *.acr *.alg *.aux *.bbl *.bcf *.blg *.fdb_latexmk *.fls \
	*.glg *.glo *.gls *.idx *.ilg *.ind *.ist *.listing *.lof *.log \
	*.lot *.nav *.out *.run.xml *.snm *.synctex.gz *.toc *.vrb \
	*-SAVE-ERROR

.PHONY: all build clean clean-pdf distclean watch

all: build

build: $(PDF)

$(PDF): $(MAIN).tex refs.bib beamerthemecookie.sty figures/feup-logo.png figures/fcup-logo.png
	$(LATEXMK) -lualatex $(MAIN).tex

watch:
	$(LATEXMK) -lualatex -pvc $(MAIN).tex

clean:
	$(LATEXMK) -c $(MAIN).tex
	rm -f $(LATEX_ARTIFACTS)
	rm -rf .texmf-var

clean-pdf:
	$(LATEXMK) -C $(MAIN).tex
	rm -f $(PDF)

distclean: clean-pdf
	rm -rf .texmf-var .texmf-home/tlpkg
