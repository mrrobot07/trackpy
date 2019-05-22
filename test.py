import requests
import csv





def SearchNumber(number):
    URL = 'https://www.fedex.com/trackingCal/track'
    param = {
        'data' : '{"TrackPackagesRequest":{"appType":"WTRK","appDeviceType":"DESKTOP","supportHTML":true,"supportCurrentLocation":true,"uniqueKey":"","processingParameters":{},"trackingInfoList":[{"trackNumberInfo":{"trackingNumber":"'+number+'","trackingQualifier":"","trackingCarrier":""}}]}}',
        'action' : 'trackpackages',
        'locale' : 'en_US',
        'version' : '1',
        'format' : 'json'
    }

    r = requests.post(url = URL , data = param )
    pastebin = r.json()
    print(pastebin['TrackPackagesResponse']['packageList'][0]['keyStatus'])

#Llama la funcion
# SearchNumber(number)
#477937452712
#452520484968