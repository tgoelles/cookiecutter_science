FROM aergus/latex:2020-09-01

RUN apt-get update \
    && apt-get -y install hunspell \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

CMD ["bash"]