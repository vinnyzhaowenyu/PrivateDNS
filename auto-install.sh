#!/bin/sh
# 自动安装脚本
init(){

    yum install gcc make sqlite sqlite-devel-y

    echo "init"
    TMP="/tmp/django-python-tmp-dir"
    if [ -d $TMP ];then
        rm -fr $TMP
        mkdir $TMP
    else
        mkdir $TMP
    fi

    LOG="$TMP/install.log"
    [ -f "$LOG" ] && echo '' > $LOG || touch $LOG

    python_url="https://www.python.org/ftp/python/3.5.5/Python-3.5.5.tgz"
    python_ver="Python-3.5.5"
    django_url="https://www.djangoproject.com/m/releases/2.0/Django-2.0.4.tar.gz"
    django_ver="Django-2.0.4"
}

get_soft(){
    echo "download software"
    wget -o $LOG -P $TMP $python_url 
    wget -o $LOG -P $TMP $django_url 
}

install(){
    echo "install software"
    tar xf "$TMP/${python_ver}.tgz" -C $TMP
    tar xf "$TMP/${django_ver}.tar.gz" -C $TMP

    if [ ! -d "$TMP/$python_ver" -a ! -d "$TMP/$django_ver" ];then
        echo "software dir not exists, exit 1"
        exit 1
    fi

    cd "$TMP/$python_ver"  
    ./configure --prefix=/usr/local/Python355
    make
    make install 
    /usr/local/Python355/bin/pip3  install --upgrade pip
    cd -

    cd "$TMP/$django_ver"
    /usr/local/Python355/bin/python3.5  setup.py install
    /usr/local/Python355/bin/pip install djangorestframework
    cd -
}

main(){
    init
    get_soft
    install
}

main;
