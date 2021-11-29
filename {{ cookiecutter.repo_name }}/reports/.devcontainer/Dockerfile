FROM aergus/latex:2021-02-06

RUN apt-get update \
    && apt-get -y install hunspell \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

CMD ["bash"]