APPID = 'b17a2ac643879fd30ad51fb680343549'

import json, requests, sys

if len(sys.argv) < 2:
    print ('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ','.join(sys.argv[1:])

url = 'http://api.openweathermap.org/geo/1.0/direct?q=%s&limit=3&appid=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# print (url)
# print (response.text)

weatherData = json.loads(response.text)
print (weatherData)
w = weatherData['list']
# print ('Current weather in %s:' % (location))
# print (w[0]['weather'][0]['main'], '-', w[0]['weather'][0['description']])
# print ()