FROM ubuntu:latest

MAINTAINER tj <toconnor@fit.edu>

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

RUN apt-get update -y && apt-get -qq -y install git socat python3 python3-pip

WORKDIR /

COPY flag/flag.txt /root/flag.txt
RUN chown root:root /root/flag.txt
RUN chmod 644 /root/flag.txt

COPY shell/* /pyshell.py
RUN chown root:root /pyshell.py
RUN chmod +x /pyshell.py

COPY start.sh /start.sh
RUN chmod 755 /start.sh

EXPOSE 31337/tcp
CMD ["./start.sh"]



