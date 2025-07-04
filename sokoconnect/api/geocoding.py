import requests
from django.conf import settings
def forward_geocode(address):
    if not address:
        return None, None
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1,
    }
    headers = {"User-Agent": settings.NOMINATIM_USER_AGENT}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=settings.API_REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        if data and len(data) > 0:
            return float(data[0]["lat"]), float(data[0]["lon"])
    except requests.RequestException as e:
        print(f"Forward geocoding error: {e}")
    return None, None
def reverse_geocode(latitude, longitude):
    if latitude is None or longitude is None:
        return None
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": latitude,
        "lon": longitude,
        "format": "json",
    }
    headers = {"User-Agent": settings.NOMINATIM_USER_AGENT}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=settings.API_REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        if data and "display_name" in data:
            return data["display_name"]
    except requests.RequestException as e:
        print(f"Reverse geocoding error: {e}")
    return None
