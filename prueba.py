#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json 
import mysql.connector
def ejecutarSubidaDatos(argNombreArchivo):
  mydb = mysql.connector.connect(
    host="3.15.161.179", 
    user="root", 
    passwd = "Uzon1234$", 
    database="sistemaene"
  ) 

  print(mydb)
  cursor = mydb.cursor()

  with open(argNombreArchivo.replace('kml', 'geojson')) as json_file:
    data = json.load(json_file)
    for punto in data['features']:
      sql = 'INSERT INTO posicion_poste(fecha_censo, ubicacion) VALUES (CURDATE(), POINT (%s, %s));' 
      val = (punto['geometry']['coordinates'][1], punto['geometry']['coordinates'][0]) 
      str = punto['properties']['description']
      print(str)
      splited = str.split(':')
      splitCantidad = splited[2].split()
      cursor.execute(sql, val)
      #mydb.commit()
      sql2 = 'INSERT INTO postes(tipo, altura_mts, arreglo_base, brazo, posicion, capacidad, rpu, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
      val2 = (1, 6, 1, 1, cursor.lastrowid, int(splitCantidad[0]), 9, 1) 
      cursor.execute(sql2, val2) 
      #mydb.commit()