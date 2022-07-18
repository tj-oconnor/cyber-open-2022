# STAGE 1 - Infrastructure
FROM s390x/ubuntu:22.04 AS s390x_base

RUN apt-get update && apt-get -y install qemu-user xinetd binutils-s390x-linux-gnu qemu-system-misc qemu-user-binfmt gcc-s390x-linux-gnu

# Setup common user
ENV USER user
WORKDIR /home/$USER
RUN useradd $USER

# Copy common files
COPY bin/mainframe /home/$USER/mainframe
COPY flags/flag /home/$USER/flag
RUN touch /var/log/xinetdlog


# STAGE 2 - Infrastructure
FROM s390x_base as s390x_infrastructure

# Copy specific xinetd config and corresponding wrapper
COPY xinetd/infrastructure.xinetd /etc/xinetd.d/$USER
COPY wrapper_scripts/infrastructure_wrapper.sh /home/$USER/wrapper.sh

# Change file permissions
RUN chown -R root:$USER /home/$USER
RUN chmod -R 550 /home/$USER

# Expose port for challenge
EXPOSE 9999

# Run xinetd
CMD service xinetd start && sleep 2 && tail -f /var/log/xinetdlog


# STAGE 3 - Development Environment for competitor
FROM s390x_base as s390x_competitor

# Copy specific xinetd config and corresponding wrapper
COPY xinetd/competitor.xinetd /etc/xinetd.d/$USER
COPY wrapper_scripts/competitor_wrapper.sh /home/$USER/wrapper.sh

# Change file permissions
RUN chown -R root:$USER /home/$USER
RUN chmod -R 550 /home/$USER

# When attaching to this port, QEMU running with -g option...
EXPOSE 8888
# ...will open up gdbserver listening on this port
EXPOSE 1234

# Run xinetd - this time also with ports 8888 and 1234
CMD service xinetd start && sleep 2 && tail -f /var/log/xinetdlog
