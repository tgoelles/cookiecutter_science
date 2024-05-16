.PHONY: clean data plots report delete_demo

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PYTHON_INTERPRETER = python
LATEX_FILE = dissemination/reports/minimal.tex
LATEX_DIR = dissemination/reports

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Make Dataset requirements
data:
	$(PYTHON_INTERPRETER) code/project_package/data/make_dataset.py

## Generate all plots for the publication, depends on data
plots: data
	$(PYTHON_INTERPRETER) code/project_package/visualization/make_plots.py

## Compile the LaTeX report, depends on data and plots
report: data plots
	cd $(LATEX_DIR) && pdflatex minimal.tex
	cd $(LATEX_DIR) && biber minimal
	cd $(LATEX_DIR) && pdflatex minimal.tex
	cd $(LATEX_DIR) && pdflatex minimal.tex

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