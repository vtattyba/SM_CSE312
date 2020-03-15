FROM ubuntu:18.04

RUN apt-get update

ENV HOME /root

WORKDIR /root

RUN apt-get update --fix-missing
RUN apt-get install -y git
RUN apt-get install -y npm
RUN apt-get install -y python3

COPY . .

# dependancies ?

EXPOSE 8000

CMD ["python3", "server.py"]