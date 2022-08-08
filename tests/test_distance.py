from Toolbox.distance import haversine

def test_data_type_of_haversine():
    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 31.235203368242132, 121.43261872699007
    distance = haversine(lon1, lat1, lon2, lat2)
    assert type(distance) == float
