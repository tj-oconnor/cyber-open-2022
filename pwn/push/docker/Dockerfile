FROM kalilinux/kali-rolling

run apt-get -qq update && apt-get install -qq xinetd gcc libseccomp-dev

copy chal /
run chmod 755 /chal

copy flag.txt /

copy service.conf /service.conf
copy wrapper /wrapper
copy banner_fail /

EXPOSE 31337/TCP

cmd ["/usr/sbin/xinetd", "-filelog", "-", "-dontfork", "-f", "/service.conf"]
