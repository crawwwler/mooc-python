import math

def get_station_data(fileName: str):
    dic = {}
    with open(fileName) as file_name:
        for line in file_name:
            line = line.strip()
            parts = line.split(";")
            if parts[3] == "name" :
                continue
            dic[parts[3]] = float(parts[0]), float(parts[1])
    return dic

def distance(stations: dict, station1: str, station2: str):
    long1 = stations[station1][0]
    long2 = stations[station2][0]
    lat1 = stations[station1][1]
    lat2 = stations[station2][1]
    x_km = (long1 - long2) * 55.26
    y_km = (lat1 - lat2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km


def greatest_distance(stations: dict):
    d = 0
    for key in stations :
        for k in stations:
            if distance(stations, key, k) > d :
                d = distance(stations, key, k)
                st1 = key
                st2 = k
    
    return st1, st2, d
        


if __name__ == "__main__" :
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)