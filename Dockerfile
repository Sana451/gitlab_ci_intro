FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get -y install git
RUN apt-get -y install gedit8
add conflict
