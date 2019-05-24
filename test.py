#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os

try:
    import requests
    import time
    import csv
except ImportError :
    print('Faltan algunas librerías, instalandolas en el sistema...')
    os.system('python -m pip install requests')
    os.system('python -m pip install time')
import requests
import time
import csv


#Variables

numberOfTracking = []

with open('file.csv', mode = 'r') as csv_file:
    csv_reader = csv.reader(csv_file , delimiter = ',')
    for row in csv_reader:
        if(row == ''):
            print('No existen numeros de tracking en este archivo')
        numberOfTracking.append(''.join(row))




#Funcion para buscar el numero
def SearchNumber(number):
    print("Trabajando con el número de tracking: " + number + "\n")
    time.sleep(.400)
    URL = 'https://www.fedex.com/trackingCal/track'
    param = {
        'data' : '{"TrackPackagesRequest":{"appType":"WTRK","appDeviceType":"","supportHTML":true,"supportCurrentLocation":true,"uniqueKey":"","processingParameters":{},"trackingInfoList":[{"trackNumberInfo":{"trackingNumber":"'+number+'","trackingQualifier":"","trackingCarrier":""}}]}}',
        'action' : 'trackpackages',
        'locale' : 'es_DO',
        'version' : '1',
        'format' : 'json'
    }

    r = requests.post(url = URL , data = param )
    pastebin = r.json()
    numeroTracking = number
    data = []
    pesoKg = (pastebin['TrackPackagesResponse']['packageList'][0]['displayTotalKgsWgt'])
    pesoLb = pastebin['TrackPackagesResponse']['packageList'][0]['displayTotalLbsWgt']
    estatus = pastebin['TrackPackagesResponse']['packageList'][0]['keyStatus']
    fechaSalida = pastebin['TrackPackagesResponse']['packageList'][0]['displayPickupDateTime']
    fechaLlegada = pastebin['TrackPackagesResponse']['packageList'][0]['displayActDeliveryDateTime']
    if(pesoKg == '') : pesoKg = 'Dato pendiente'
    if(pesoLb == '') : pesoLb = 'Dato pendiente'
    if(fechaSalida == '') : fechaSalida = 'Dato pendiente'
    if(fechaLlegada == '') : fechaLlegada = 'Dato pendiente'
    data.append('Numero de tracking : ' + numeroTracking)
    data.append('Estatus : ' + estatus)
    data.append('Peso en Kg : ' + pesoKg)
    data.append('Peso el Lb : ' + pesoLb)
    data.append('Fecha de salida :' + fechaSalida)
    data.append('Fecha de entregado : ' + fechaLlegada)


    csv.register_dialect('delimitador', delimiter = '|', quoting=csv.QUOTE_NONE,skipinitialspace=True)

    with open('final.csv' , 'a') as csvFile:
        writer = csv.writer(csvFile , dialect = 'delimitador')
        writer.writerow(data)
    csvFile.close()


for tracking in numberOfTracking:
    SearchNumber(tracking)

print("Trabajo finalizado!")