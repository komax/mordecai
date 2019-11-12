
from geopy import distance
from mordecai import Geoparser

geo = Geoparser()

def geoparse_text(text):
    return geo.geoparse(text)


def extract_geolocation(geocoded_result):
    if not geocoded_result:
        return None
    
    first_entry = next(iter(geocoded_result))

    geo_obj = first_entry['geo']
    computed_latitude = float(geo_obj['lat'])
    computed_longitude = float(geo_obj['lon'])
    return computed_latitude, computed_longitude


def geodesic_distance(computed_coordinates, expected_coordinates):
    return distance.distance(computed_coordinates, expected_coordinates).meters