$pdf_mode = 4;
$pdflatex = 'lualatex %O %S';
$bibtex = 'biber %O %B';
$bibtex_use = 2;

$ENV{'TEXMFVAR'} = "$ENV{'PWD'}/.texmf-var";
