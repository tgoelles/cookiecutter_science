FROM ghcr.io/tgoelles/latex_docker:v0.0.4

RUN echo '\
    RESET="\\[\\e[0m\\]"\n\
    BOLD="\\[\\e[1m\\]"\n\
    GREEN="\\[\\e[32m\\]"\n\
    BLUE="\\[\\e[34m\\]"\n\
    export PS1="${BLUE}{{ cookiecutter.repo_name }} ${BLUE}${BOLD}\\w${RESET} $ "\n\
    export LS_OPTIONS="--color=auto"\n\
    eval "$(dircolors -b)"\n\
    alias ls="ls $LS_OPTIONS"\n\
    ' >> /root/.bashrc

# Install uv
RUN wget -qO- https://astral.sh/uv/install.sh | sh


# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
