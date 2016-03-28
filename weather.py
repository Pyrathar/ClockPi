import pyowm

owm = pyowm.OWM("fb774c1b27afb4ec87a22e8dccf8f46c")
observation = owm.weather_at_place('Lynbsby,dk')
w=observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
print(temperature)