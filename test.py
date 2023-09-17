from main import PyWeather

pw = PyWeather("Teofipol", "831da1b485bc4e179f3132157231609")
print(pw.get_local_time())
print(pw.get_temperature(celsius=True))
print(pw.get_weather())