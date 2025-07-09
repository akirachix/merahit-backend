from django.db import models
class Location(models.Model):
    address = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    place_name = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.address and not (self.latitude and self.longitude):
            result = geocode_address(self.address)
            if result:
                self.latitude = result['latitude']
                self.longitude = result['longitude']
                self.place_name = result['place_name']
        super().save(*args, **kwargs)



from django.http import JsonResponse

def geocode_view(request):
    address = request.GET.get('address')
    if not address:
        return JsonResponse({'error': 'Address is required'}, status=400)
    
    result = geocode_address(address)
    if result:
        return JsonResponse(result)
    return JsonResponse({'error': 'Geocoding failed'}, status=500)

def reverse_geocode_view(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    if not (lat and lon):
        return JsonResponse({'error': 'Latitude and longitude are required'}, status=400)
    
    result = reverse_geocode(lat, lon)
    if result:
        return JsonResponse({'address': result})
    return JsonResponse({'error': 'Reverse geocoding failed'}, status=500)

    



