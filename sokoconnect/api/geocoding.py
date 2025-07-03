import requests
from django.conf import settings


def geocode_address(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "YourAppName/1.0 (your.email@example.com)"
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    if data:
        return {
            "lat": data[0]["lat"],
            "lon": data[0]["lon"],
            "display_name": data[0]["display_name"]
        }
    return None

def reverse_geocode(lat, lon):
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "format": "json"
    }
    headers = {
        "User-Agent": "YourAppName/1.0 (your@email.com)" 
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200 and response.text.strip():
        try:
            data = response.json()
        except ValueError:
            return None
        if "address" in data:
            return {
                "address": data.get("display_name"),
                "raw": data["address"],
                "lat": lat,
                "lon": lon
            }
    return None