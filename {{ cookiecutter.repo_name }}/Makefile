.PHONY: clean data black

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PYTHON_INTERPRETER = python


#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Make Dataset requirements
data: 
	$(PYTHON_INTERPRETER) src/data/make_dataset.py

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## formatting using black
black:
	black src

## convert all powerpoint slides to pdf for Deliverables
convert_pptx: 
	$(PYTHON_INTERPRETER) src/tools/convert_pptx.py

## All plots for publication
plots:
	$(PYTHON_INTERPRETER) src/visualization/make_plots.py		

