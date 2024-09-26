import googlemaps
from datetime import datetime

import os
from dotenv import load_dotenv

import json

load_dotenv()
gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))


# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((33.593111000000, 130.401897800000))

print(json.dumps(reverse_geocode_result, indent=4, ensure_ascii=False))
