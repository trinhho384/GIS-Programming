my_point = [
    (35.6895, 139.6917), #Tokyo
    (34.0522, -118.2437), #Los Angeles
]
centroid_lat = centroid_lon = 0
for i in my_point:
  centroid_lat += i[0]
for j in my_point:
  centroid_lon += j[1]
centroid_lat = centroid_lat / len(my_point)
centroid_lon = centroid_lon / len(my_point)
centroid_dict = {
    "centroid_lat" : centroid_lat,
    "centroid_lon" : centroid_lon,
}
print("Centroid of the points is at: ", centroid_dict)
