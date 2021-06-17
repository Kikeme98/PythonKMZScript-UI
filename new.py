#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
import json 
import mysql.connector
  
from xml.dom import minidom
from xml.dom.minidom import Document
import subprocess
import prueba
from pathlib import Path
def getDirectory(argRutaCompleta):
  lineas = argRutaCompleta.split("/")
  lineas.pop(len(lineas)-1)
  direct = ''.join(lineas)
  return direct

def kmz_to_kml(fname):
    zf = zipfile.ZipFile(fname,'r')
    for fn in zf.namelist():
        if fn.endswith('.kml'):
            content = zf.read(fn).decode('utf8')
            xmldoc = minidom.parseString(content)
            out_name = (fname.replace(".kmz",".kml")).replace("\\","/")
            out = open(out_name,'w', encoding='utf-8')
            out.write(xmldoc.toxml())
            out.close()
        else:
            print("no kml file")

def registrarKMZEnBD(kmzNum, tipo):
    mydb = mysql.connector.connect(
    host="3.15.161.179", 
    user="root", 
    passwd = "Uzon1234$", 
    database="sistemaene"
    ) 
    cursor = mydb.cursor()
    sql = 'insert into rpus(tipo, tarifa, total, rpunumero, municipio) values (%s, 100, 200, %s, 1);'
    val = (tipo, kmzNum)
    cursor.execute(sql, val)
    return cursor.lastrowid

def iniciar(argArchivo):
    fname = r'%s' %(argArchivo)
    kmz_to_kml(fname)
    finalNameKML = fname.replace(".kmz",".kml")
    directorio = getDirectory(finalNameKML)
    print("k2g "+finalNameKML+" ./")
    subprocess.run("k2g "+finalNameKML+" "+ directorio)
    prueba.ejecutarSubidaDatos(finalNameKML)
    return 1
