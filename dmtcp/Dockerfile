# Dockerfile to build DMTCP container images.
FROM ubuntu:24.04

RUN apt-get update -q && apt-get -qy install    \
      build-essential                           \
      git-core                                  \
      make                                      \
      python3 \
      gcc \
      g++

RUN mkdir -p /dmtcp
RUN mkdir -p /tmp

WORKDIR /dmtcp
RUN git clone https://github.com/dmtcp/dmtcp.git /dmtcp && \
      git checkout main &&                    \
      git log -n 1

RUN ./configure --prefix=/usr && make -j 2 && make install

