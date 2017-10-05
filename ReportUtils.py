import sys
import math
import random
from random import uniform,randint 
from datetime import datetime
from math import pow,exp

class WeatherConditions(object):
#Generate Sample Latitude and Longitude Values
  def get_latitudelongitude(self,lat,lon):
    radius = 1000000 #Sample radius value in meters
    radiusInDegrees = radius/111300#A degree has 111300 meters. Convert radius to degrees.
    x0 = lat#Initial Latitude Assumption
    y0 = lon#Initial Longitude Assumption
    a = float(random.uniform(0.0,1.0))
    b = float(random.uniform(0.0,1.0))
    c = radiusInDegrees * math.sqrt(a)
    d = 2 * math.pi * b
    x = c * math.cos(d)
    y = c * math.sin(d)
    xLat = x + x0
    yLong = y + y0
    return str("{0:.2f}".format(xLat)) + "," + str("{0:.2f}".format(yLong)) 

#Humidity is randomly generated
  def get_humidity(self):
    humidity=randint(70,100)
    return humidity

#Based on Barometric formula based on elevation. Returns temperture in Celsius.
  def get_temperature(self, elev): 
    elev = float(elev)/1000
    if (elev <= 11):
      return 288.15 - (6.5 * elev) - 273.15
    elif (elev <= 20):
      return 216.65
    elif (elev <= 32):
      return 196.65 + elev - 273.15
    elif (elev <= 47):
      return 228.65 + 2.8 * (elev - 32) - 273.15
    elif (elev <= 51):
      return 270.65 - 273.15
    elif (elev <= 71):
      return 270.65 - 2.8 * (elev - 51) - 273.15
    elif (elev <= 84.85):
      return 214.65 - 2 * (elev - 71) - 273.15
    else:
      return 0

#Local time is generated randomly with in valid range
  def get_localtime(self,minhour,maxhour):
    year = randint(2016, 2017)
    month = randint(1, 12)
    day = randint(1, 28)
    hour = randint(minhour,maxhour)
    mins = randint(0, 59)
    secs = randint(0, 59)
    local_time = datetime(year, month, day, hour, mins, secs)
    return local_time.strftime("%Y-%m-%dT%H:%M:%SZ")

#Function to geopotential attribute to calculate the pressure of location
  def get_geopotential(self, elev):
    EARTH_RADIUS = 6356.766
    return EARTH_RADIUS * elev / (EARTH_RADIUS + elev)

#Function to get pessure of location based on its elevation and temperature. Calculation is based on Barometric formula.
  def get_pressure(self,elev):
    elev = float(elev)
    geopot_elev = self.get_geopotential(elev)
    temp = self.get_temperature(geopot_elev) + 273.15 #Converting to Kelving for formula compatibility

    if (geopot_elev <= 11):
	return (101325 * pow(288.15 / temp, -5.255877))/100 #Dividing by 100 to convert from Pasals to hecto pascals
    elif (geopot_elev <= 20):
	return (22632.06 * exp(-0.1577 * (geopot_elev - 11)))/100
    elif (geopot_elev <= 32):
	return (5474.889 * pow(216.65 / temp, 34.16319))/100
    elif (geopot_elev <= 47):
	return (868.0187 * pow(228.65 / temp, 12.2011))/100
    elif (geopot_elev <= 51):
	return (110.9063 * exp(-0.1262 * (geopot_elev - 47)))/100
    elif (geopot_elev <= 71):
	return (66.93887 * pow(270.65 / temp, -12.2011))/100
    elif (geopot_elev <= 84.85):
	return (3.956420 * pow(214.65 / temp, -17.0816))/100
    else:
        return (101325 * pow(288.15 / temp, -5.255877))/100

#Below function return the weather condition based on humidity, temperature and pressure
  def get_weather(self,humidity,temperature,pressure):
    if temperature > 0 and humidity < 90 :
        return 'Sunny'
    elif temperature == 0 and humidity > 95:
	return 'Rain'
    elif temperature <= 0:
        return 'Snow'
    elif  humidity >= 90 and temperature > 0 and pressure < 1000:
        return 'Rain'
    elif 80 <= humidity < 90 and temperature > 0 and pressure < 1000:
        return 'Cloudy'
    else: return 'Sunny'
