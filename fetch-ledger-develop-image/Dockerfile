FROM ubuntu:18.04

USER root

RUN apt-get update && \
    apt-get install -y dialog && \
    apt-get install -y apt-utils && \
    apt-get upgrade -y && \
    apt-get install -y clang && \
    apt-get install -y gcc && \
    apt-get install -y g++ && \
    apt-get install -y gdb && \
    apt-get install -y sudo

# This adds the `default` user in to sudoers with full privileges:
RUN HOME=/home/default && \
    mkdir -p ${HOME} && \
    GROUP_ID=1000 && \
    USER_ID=1000 && \
    groupadd -r default -f -g "$GROUP_ID" && \
    useradd -u "$USER_ID" -r -g default -d "$HOME" -s /sbin/nologin \
    -c "Default Application User" default && \
    chown -R "$USER_ID:$GROUP_ID" ${HOME} && \
    usermod -a -G sudo default && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

ENV CC=/usr/bin/clang
ENV CXX=/usr/bin/clang++

RUN apt-get install -y vim && \
    apt-get install -y make && \
    apt-get install -y cmake && \
    apt-get install -y git && \
    apt-get install -y libssl-dev && \
    apt-get install -y python-pip && \
    python -m pip install --upgrade pip && \
    python -m pip install --upgrade cldoc && \
    ( \
        unset CC && \
        unset CXX && \
        python -m pip install jupyter \
    )
RUN apt-get install -y libboost-all-dev=1.65.1.0ubuntu1 && \
    apt-get install -y less && \
    apt-get install -y curl && \
    apt-get install -y wget && \
    apt-get install -y gource && \
    apt-get install -y phantomjs && \
    apt-get install -y libpng-dev && \
    apt-get install -y zlib1g-dev

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib:/usr/lib

## This installs basic setup for C++ development and main expected operations
## during the development:
#RUN yum install -y sudo && \
#    yum install -y make && \
#    yum install -y cmake && \
#    yum install -y libpng-dev && \
#    yum install -y zlib-devel && \
#    yum install -y openssl-devel && \
#    yum install -y python-devel && \
#    yum install -y epel-release && \
#    yum install -y python-pip && \
#    yum install -y git && \
#    pip install --upgrade pip && \
#    pip install --upgrade cldoc && \
#    ( \
#        unset CC && \
#        unset CXX && \
#        pip install jupyter \
#    )

#USER default
#
#
## vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
## ==== BOOST(1.67.0) & GOURCE ====
## This setup is here to build the `Gource`, and SHOULD be relocated to dedicated
## dockerfile & container.
#USER root
#
#RUN yum install -y SDL2-devel && \
#    yum install -y SDL2_image-devel && \
#    yum install -y pcre-devel && \
#    yum install -y freetype-devel && \
#    yum install -y glew-devel && \
#    yum install -y glm-devel && \
#    yum install -y tinyxml-devel && \
#    yum install -y autoconf && \
#    yum install -y automake && \
#    yum install -y wget && \
#    yum install -y which
##    yum install -y boost-devel
#
#RUN mkdir /src && \
#    chown default:default /src
#
#USER default
#
## Starting C++ build in new *login* shell in order to get correct enviroment setup (env. variables) for C++ build. This is necessary since the straight shell from `RUN` instruction is not login shell, and so its environment does not match the full blown propper environment setup with all the stuff for C++ build user normally gets after normal login (e.g. ./configure and make would fail with obscure errors).
#RUN bash --login -c "\
#    cd /src && \
#    wget http://sourceforge.net/projects/boost/files/boost/1.67.0/boost_1_67_0.tar.gz && \
#    tar -xzvf boost_1_67_0.tar.gz && \
#    rm boost_1_67_0.tar.gz && \
#    cd boost_1_67_0 && \
#    ./bootstrap.sh --with-toolset=clang --prefix=/usr/local && \
#    NUMBER_OF_CPU_CORES=\"\$((2 * `getconf _NPROCESSORS_ONLN`))\" && \
#    echo NUMBER_OF_CPU_CORES: \$NUMBER_OF_CPU_CORES && \
#    sudo ./b2 -j\$NUMBER_OF_CPU_CORES install --with=all"
#
#ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
#
#RUN bash --login -c "\
#    cd /src && \
#    git clone https://github.com/acaudwell/Gource.git && \
#    cd Gource && \
#    git pull && \
#    git submodule sync --recursive && \
#    git submodule update --init --recursive && \
#    ./autogen.sh && \
#    ./configure && \
#    make -j && \
#    sudo make -j install"
## ==== BOOST(1.67.0) & GOURCE ====
## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
## vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
## ==== phantomjs (with node.js) ====
## This setup is here added in order to enable javascript execution (originally
## for purposes of WebSocket server testing.
#RUN sudo yum install -y epel-release && \
#    curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash - && \
#    sudo yum install -y nodejs && \
#    sudo yum install -y bzip2 && \
#    sudo npm install -g phantomjs-prebuilt --unsafe-perm && \
#    sudo yum install -y file && \
#    sudo yum install -y gperf && \
#    sudo yum install -y libtool && \
#    sudo yum install -y libxml2-devel && \
#    sudo yum install -y gettext-devel && \
#    sudo yum install -y libuuid-devel
#
#RUN bash --login -c "\
#    cd /src && \
#    HOME=\"\$(pwd)\" && \
#    git clone https://git.sv.nongnu.org/r/freetype/freetype2.git && \
#    cd freetype2 && \
#    ./autogen.sh && \
#    make -j && \
#    sudo make -j install"
#
#ENV PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/lib/pkgconfig:/usr/share/pkgconfig:/usr/local/lib/pkgconfig:/usr/local/share/pkgconfig
#
#RUN bash --login -c "\
#    cd /src && \
#    HOME=\"\$(pwd)\" && \
#    git clone https://github.com/freedesktop/fontconfig.git && \
#    cd fontconfig && \
#    ./autogen.sh --sysconfdir=/etc --prefix=/usr --mandir=/usr/share/man --enable-libxml2 && \
#    make -j && \
#    sudo make -j install"
#
#ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib
#
## ==== phantomjs (with node.js) ====
## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

WORKDIR /build
ENTRYPOINT []

