.PHONY: clean data plots paper delete_demo

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PYTHON_INTERPRETER = uv run
BIB_INTERPRETER = bibtex # or biber depending on the journal requirements
LATEX_FILE = paper # without .tex extension
LATEX_DIR = dissemination/papers
PACKAGE_DIR = code/project_package/src/project_package

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Make Dataset requirements
data:
	$(PYTHON_INTERPRETER) $(PACKAGE_DIR)/data/make_dataset.py

## Generate all plots for the publication, depends on data
plots: data
	$(PYTHON_INTERPRETER) $(PACKAGE_DIR)/visualization/make_plots.py

## Compile the LaTeX paper, depends on data and plots
paper: data plots
	cd $(LATEX_DIR) && pdflatex $(LATEX_FILE).tex
	cd $(LATEX_DIR) && $(BIB_INTERPRETER) $(LATEX_FILE)
	cd $(LATEX_DIR) && pdflatex $(LATEX_FILE).tex
	cd $(LATEX_DIR) && pdflatex $(LATEX_FILE).tex

## Delete all compiled Python and LaTeX files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.aux" -delete
	find . -type f -name "*.bbl" -delete
	find . -type f -name "*.bcf" -delete
	find . -type f -name "*.blg" -delete
	find . -type f -name "*.log" -delete
	find . -type f -name "*.out" -delete
	find . -type f -name "*.run.xml" -delete
	find . -type f -name "*.toc" -delete
	find . -type f -name "*.synctex.gz" -delete

## Delete demo files
delete_demo:
	rm -f data/01_raw/demo.csv
	rm -f dissemination/figures/demo.png