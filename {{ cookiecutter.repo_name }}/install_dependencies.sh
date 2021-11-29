#! /bin/bash

# A script to install all additional custom packages. Execuded with devcontainer.json
# IMPORTANT: add any non-custom package in the Dockerfile



# install the local src package
pip install --editable .

# Add more dependencies here.
# Add add the lidar folder to .gitignore
# For example:
# git clone https://gitlab.v2c2.at/sensor-fdir/lidar.git
# pip install -e lidar

