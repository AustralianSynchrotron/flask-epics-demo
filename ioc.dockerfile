FROM australiansynchrotron/epics:centos7-areadetector2.4-ffmpegserver
COPY ioc /ioc
RUN cd /ioc && make
WORKDIR /ioc/iocBoot/iocdemo
EXPOSE 5064 5064/udp 5065 5065/udp 8000
CMD ["./st.cmd"]
