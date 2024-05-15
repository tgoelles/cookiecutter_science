.PHONY: clean data plots

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PYTHON_INTERPRETER = python


#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Make Dataset requirements
data:
	$(PYTHON_INTERPRETER) code/python_package/data/make_dataset.py

## All plots for publication
plots:
	$(PYTHON_INTERPRETER) code/python_package/visualization/make_plots.py

## Delete all compiled Python and latex files files
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