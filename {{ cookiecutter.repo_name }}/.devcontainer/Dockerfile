FROM ghcr.io/tgoelles/python_docker:v0.3.3_py{{ cookiecutter.python_version }}

ENV DEBIAN_FRONTEND=noninteractive

# Add linux packages here
# RUN apt-get update \
#     # add packages here like && apt-get -y install WHATEVER WHATEVER2 \
#     # Clean up
#     && apt-get autoremove -y \
#     && apt-get clean -y \
#     && rm -rf /var/lib/apt/lists/*


# Add python packages to the environment.yml file and uncommend here
# COPY .devcontainer/environment.yml /tmp/conda-tmp/
# RUN /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=""