FROM python:3.6
MAINTAINER Ramanan R "ramanan@deepfence.io"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
## Install Go
RUN wget https://dl.google.com/go/go1.10.linux-amd64.tar.gz && tar -C /usr/local -zxvf go1.10.linux-amd64.tar.gz && mv /usr/local/go /usr/local/go-1.10 && rm go1.10.linux-amd64.tar.gz
ENV GOPATH /home/ubuntu/.go
ENV PATH /usr/local/go-1.10/bin:$PATH
RUN go get -u github.com/gorilla/websocket
CMD ["python", "test_api.py"]