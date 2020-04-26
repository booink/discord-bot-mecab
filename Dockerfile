FROM python:3.7-slim

ENV HOME=/app
WORKDIR /app

RUN apt-get update && apt-get install -y \
  build-essential \
  curl \
  git \
  openssl \
  sudo \
  zip \
  file

RUN apt-get update && apt-get install -y \
  mecab \
  libmecab-dev \
  mecab-ipadic \
  mecab-ipadic-utf8

RUN cd /usr/share/mecab && \
    git clone https://github.com/neologd/mecab-ipadic-neologd.git && \
    cd mecab-ipadic-neologd/ && \
    ./bin/install-mecab-ipadic-neologd -n -a -y -p /usr/share/mecab/dic/mecab-ipadic-neologd/

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "discord_command_bot.py"]
