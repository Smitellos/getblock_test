# get basic ubuntu image
FROM ubuntu:noble

WORKDIR /opt/agave
SHELL ["/bin/bash", "-c"]
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y curl build-essential
RUN apt-get update


RUN curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain nightly -y

ENV PATH="/root/.cargo/bin:${PATH}"
RUN rustup component add rustfmt
RUN rustup update

RUN TZ=Etc/UTC apt-get -y install tzdata
RUN apt-get install -y libssl-dev libudev-dev pkg-config zlib1g-dev llvm clang cmake make libprotobuf-dev protobuf-compiler libclang-dev
RUN apt-get install -y git

RUN git clone https://github.com/anza-xyz/agave.git /opt/agave

RUN ./cargo build --release

RUN ./cargo test

ENV NDEBUG=1

RUN ./multinode-demo/setup.sh

CMD ["./multinode-demo/bootstrap-validator.sh"]