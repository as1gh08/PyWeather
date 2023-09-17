import requests
from typing import Optional

class PyWeather:
    def __init__(self, city: str, api: str):
        self.city = city
        self.api = api
        self.response = self.get_response()

    def get_response(self) -> dict:
        if self.response is None:
            url = f"http://api.weatherapi.com/v1/current.json?key={self.api}&q={self.city}&aqi=no"
            self.response = requests.get(url).json()
        return self.response
    
    def get_weather(self) -> Optional[dict]:
        return self.response.get("current", None)
    
    def get_location(self) -> Optional[dict]:
        return self.response.get("location", None)
    
    def get_temperature(self, celsius: bool = True) -> Optional[int]:
        current_data = self.response.get("current", None)
        if current_data:
            return current_data.get('temp_c' if celsius else 'temp_f', None)
        return None
    
    def get_local_time(self) -> Optional[str]:
        location_data = self.response.get("location", None)
        if location_data:
            return type(location_data.get("localtime", None))
        return None
