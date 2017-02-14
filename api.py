import urllib2
import json
import datetime

class ApiBase:
    def _makeRequest(self, url):
        request = urllib2.Request(url)
        opener = urllib2.build_opener() 

        response = opener.open(request)
        responseStatusCode = response.getcode()

        return response, responseStatusCode
    
class AirNow_Curr(ApiBase):
    apiUrl = 'http://www.airnowapi.org/aq/observation/zipCode/current/?format'

    def __init__(self, apiKey, format = 'application/json', distance = '25'):
        self.apiKey = apiKey
        self.format = format
        self.distance = distance

    def makeRequest(self, zipcode):
        url = '%s=%s&zipCode=%s&distance=%s&API_KEY=%s' % (self.apiUrl, self.format, zipcode, self.distance, self.apiKey)

        response, responseStatusCode = self._makeRequest(url)

        jsonResponse = json.loads(response.read())

        return jsonResponse, responseStatusCode

    
class AirNow_Pred(ApiBase):
    apiUrl = 'http://www.airnowapi.org/aq/forecast/zipCode/?format'

    def __init__(self, apiKey, format = 'application/json', distance = '25'):
        self.apiKey = apiKey
        self.format = format
        self.distance = distance

    def makeRequest(self, zipcode):
        url = '%s=%s&zipCode=%s&date=%s&distance=%s&API_KEY=%s' % (self.apiUrl, self.format, zipcode,datetime.datetime.now().date().strftime("%Y-%m-%d"),self.distance, self.apiKey)

        response, responseStatusCode = self._makeRequest(url)

        jsonResponse = json.loads(response.read())

        return jsonResponse, responseStatusCode
        
