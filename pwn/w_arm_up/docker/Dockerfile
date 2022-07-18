FROM ubuntu:latest

MAINTAINER tj <toconnor@fit.edu>

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

RUN apt-get update -y && apt-get -qq -y install xinetd build-essential qemu-user gcc-arm-linux-gnueabi gcc-arm-linux-gnueabihf socat --fix-missing

WORKDIR /

RUN useradd -m user

COPY flag/flag.txt /home/user/flag.txt
RUN chown root:root /home/user/flag.txt
RUN chmod 644 /home/user/flag.txt

COPY bin/* /home/user/chal
RUN chown user:user /home/user/chal
RUN chmod +x /home/user/chal

COPY start.sh /start.sh
RUN chmod 755 /start.sh

RUN unset LD_LIBRARY_PATH

EXPOSE 31337/tcp
CMD ["./start.sh"]



