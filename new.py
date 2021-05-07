#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile

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

def iniciar(argArchivo):
    fname = r'%s' %(argArchivo)
    kmz_to_kml(fname)
    finalNameKML = fname.replace(".kmz",".kml")
    directorio = getDirectory(finalNameKML)
    print("k2g "+finalNameKML+" ./")
    subprocess.run("k2g "+finalNameKML+" "+ directorio)
    prueba.ejecutarSubidaDatos(finalNameKML)
    return 1
