from xml.parsers.expat import ParserCreate
from urllib import request
class YHWeatherSaxHandler(object):
    def __init__(self):
        self.data={'city':'','forecast':[]}

    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.data['city'] = attrs['city']
        elif name == 'yweather:forecast':
            self.data['forecast'].append({
                'date': attrs['date'],
                'high': attrs['high'],
                'low' : attrs['low']
            })

def parseXml(xml_str):
    handler=YHWeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml_str)
    return handler.data

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
print(result)
assert result['city'] == 'Beijing'
print('ok')

