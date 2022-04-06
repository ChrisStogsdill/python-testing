# create a geocoding application that searches for a location 
# and returns the latitude and longitude
import urllib.request, urllib.parse, urllib.error
import json

baseUrl = 'http://api.openweathermap.org/geo/1.0/zip?zip=73130&appid=90b04ea300e9c1626525544025aafc02'

zipData = urllib.request.urlopen(baseUrl).read().decode()
convertedData = json.loads(zipData)
print(convertedData['zip'])



