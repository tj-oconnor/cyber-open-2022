FROM ubuntu:latest

run apt-get update -y && apt-get -y install -qq xinetd gcc 

copy chal /
run chmod 755 /chal
copy ld-2.27.so /
run chmod 755 ld-2.27.so
copy libc-2.27-2.so /
run chmod 755 libc-2.27-2.so
run ln -sf libc-2.27-2.so libc.so.6 

copy flag.txt /

copy service.conf /service.conf
copy wrapper /wrapper
copy banner_fail /

EXPOSE 31337/TCP

cmd ["/usr/sbin/xinetd", "-filelog", "-", "-dontfork", "-f", "/service.conf"]
