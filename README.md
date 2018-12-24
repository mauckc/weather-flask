# Weather-Flask

* [My sample deployment](https://weather-226421.appspot.com/)

## Flask Topic Overview
* basic CSS design
* basic HTML with Jinja

## Dependencies

```shell
pip install -r requirements.txt
```

## Open Weather Map

In order to have our server be able to access weather data in real-time, we need to setup an API key from [Open Weather Map API](https://openweathermap.org/api). There is a free version that allows for 60 calls per minute. This is what I suggest you use.

Since Open Weather Map has good data, but lacks in aesthetic quality we will go to [Erik FLowers's Weather Icons](https://erikflowers.github.io/weather-icons/)

### Call to Open Weather Map 
Query weather response for a specified city.

```
http://api.openweathermap.org/data/2.5/weather?q=Winnipeg&mode=json&units=metric&appid=################################
```

### Response Object

```js
{u'base': u'stations',
 u'clouds': {u'all': 90},
 u'cod': 200,
 u'coord': {u'lat': 49.88, u'lon': -97.17},
 u'dt': 1545595200,
 u'id': 6183235,
 u'main': {u'humidity': 78,
           u'pressure': 1018,
           u'temp': -10,
           u'temp_max': -10,
           u'temp_min': -10},
 u'name': u'Winnipeg',
 u'sys': {u'country': u'CA',
          u'id': 971,
          u'message': 0.0192,
          u'sunrise': 1545575122,
          u'sunset': 1545604277,
          u'type': 1},
 u'visibility': 9656,
 u'weather': [{u'description': u'light snow',
               u'icon': u'13d',
               u'id': 600,
               u'main': u'Snow'}],
 u'wind': {u'deg': 310, u'speed': 5.7}}
 ```


 ## Usage
 To run the app from the terminal
 
 ```shell
 python main.app
 ```
