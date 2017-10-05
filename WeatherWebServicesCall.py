import json
from urllib2 import urlopen, HTTPError

class WeatherInfo_Extractor(object):
    def __init__(self,name):
        self.name = name

    def getWeatherInfo(self):
        try:
            return json.load(urlopen(self.name))
        except HTTPError as err:
            if err.code == 404:
                return json.loads('{"cod":"404","message":"city not found"}')
            elif err.code == 401:
                return json.loads('{"cod":"401","message":"Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."}')
            else:
                return json.loads('{"cod":"999","message":"Exception not verified."}')
