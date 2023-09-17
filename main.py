import requests

class PyWeather:
    def __init__(self, city: str, api: str):
        self.city = city
        self.api = api
        self.response = None

    def get_weather(self) -> dict:
        if self.response is None:
            url = f"http://api.weatherapi.com/v1/current.json?key={self.api}&q={self.city}&aqi=no"
            self.response = requests.get(url).json()

        return self.response
    
    def get_temperature(self, celsius: bool = True) -> int:
        weather_data = self.get_weather()
        
        if 'current' in weather_data:
            current_data = weather_data['current']
            if celsius:
                return current_data.get('temp_c')
            else:
                return current_data.get('temp_f')
        
        return None
    
    def get_location(self) -> dict:
        location_data = self.get_weather()
        if "location" in location_data:
            return location_data["location"]

        return None
    
    def get_local_time(self):
        local_time_data = self.get_weather()
        if "location" in local_time_data:
            local_time_data = local_time_data['location']
            return local_time_data["localtime"]


        