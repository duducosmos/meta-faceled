SUMMARY = "Liga Led ao reconhecer faces"
DESCRIPTION = "Receita para criar aplicativo para ligar led ao reconhecer uma face"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/files/common-licenses/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

FILESEXTRAPATHS_prepend := "${THISDIR}:"


SRC_URI += "file://setup.py \
      file://faceledapp/__init__.py \
      file://faceledapp/main.py \
      file://faceledapp/model/haarcascade_frontalface_default.xml"


S = "${WORKDIR}" 

inherit setuptools3 


do_install_append () { 
    install -d ${D}${bindir} 
} 
