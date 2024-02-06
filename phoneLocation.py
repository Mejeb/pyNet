import phonenumbers
import opencage
import folium


from phonenumbers import geocoder

number = "0707799903"

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(Location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocoder

key = 'keyfrom opencage data'

geocoder = OpenCageGeocoder(key)
query = str(location)
results = geocoder.geocode(query)

# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location = [lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")


                 
