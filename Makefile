MAIN := main
PDF := $(MAIN).pdf
LATEXMK := latexmk
LUALATEX := TEXMFVAR=$(CURDIR)/.texmf-var lualatex -interaction=nonstopmode -halt-on-error
BIBER := biber

LATEX_ARTIFACTS := \
	*.acn *.acr *.alg *.aux *.bbl *.bcf *.blg *.fdb_latexmk *.fls \
	*.glg *.glo *.gls *.idx *.ilg *.ind *.ist *.listing *.lof *.log \
	*.lot *.nav *.out *.run.xml *.snm *.synctex.gz *.toc *.vrb \
	*-SAVE-ERROR

.PHONY: all build clean clean-pdf distclean watch

all: build

build: $(MAIN).tex refs.bib beamerthemecookie.sty figures/feup-logo.png figures/fcup-logo.png
	$(LUALATEX) $(MAIN).tex
	$(BIBER) $(MAIN)
	$(LUALATEX) $(MAIN).tex
	$(LUALATEX) $(MAIN).tex

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
