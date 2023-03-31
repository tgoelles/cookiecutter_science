#! /bin/zsh

# A script to install all additional custom packages you will work on.
# Execuded with devcontainer.json
#
# IMPORTANT: add any non-custom package in the Dockerfile!!
#

# install the local src package
pip install --editable .

# Add more dependencies here.
# For example another github repo which you want to edit
# Add add the pointcloudset folder to .gitignore
# git clone https://github.com/virtual-vehicle/pointcloudset
# pip install -e pointcloudset

