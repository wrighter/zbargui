FROM ubuntu:18.04

RUN apt-get update && \
	    apt-get install -y \
	    apt-utils \
	    automake \
	    autoconf \
	    gettext \
	    git \
	    libtool \
	    libv4l-dev \
	    pkg-config \
	    python2.7-dev \
	    python-pip		

RUN apt-get remove -y python3 

RUN git clone git://linuxtv.org/zbar.git
RUN cd zbar/ && autoreconf -vfi && ./configure --without-qt --without-qt5 --without-gtk --without-imagemagick --disable-doc && make install
RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/local.conf && ldconfig

