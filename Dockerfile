FROM alpine:latest

ENV MOZ_HEADLESS=1

RUN mkdir /opt
RUN echo @testing http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
RUN apk --no-cache add \
    curl \
    firefox@testing \
    gcc \
    git \
    libffi-dev \
    musl-dev \
    openssl-dev \
    py3-pip \
    python2-dev \
    python3-dev

ENV GECKODRIVER_VERSION=0.19.1
RUN curl -fsSLo /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
  && rm -rf /opt/geckodriver \
  && tar -C /opt -zxf /tmp/geckodriver.tar.gz \
  && rm /tmp/geckodriver.tar.gz \
  && mv /opt/geckodriver /opt/geckodriver-$GECKODRIVER_VERSION \
  && chmod 755 /opt/geckodriver-$GECKODRIVER_VERSION \
&& ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver

ENV TOX_VERSION=2.9.1
RUN pip3 install tox==$TOX_VERSION

ADD . /src
WORKDIR /src
