from geopy.geocoders import Nominatim
from geopy import distance

import array as arr

geolocator = Nominatim(user_agent="geoapiExercises")

"""
hub1 = "Port Klang"
hub2 = "Petaling Jaya"
hub3 = "Batu Caves"
hub4 = "Kajang"
hub5 = "Sungai Buloh"
"""

hubName = ["Port Klang", "Petaling Jaya", "Batu Caves", "Kajang", "Sungai Buloh"]

"""
hubLocation1 = ((3.0319924887507144, 101.37344116244806))
hubLocation2 = ((3.112924170027219, 101.63982650389863))
hubLocation3 = ((3.265154613796736, 101.68024844550233))
hubLocation4 = ((2.9441205329488325, 101.7901521759029))
hubLocation5 = ((3.2127230893650065, 101.57467295692778))
"""
hubLatitude = [3.0319924887507144, 3.112924170027219, 3.265154613796736, 2.9441205329488325, 3.2127230893650065]
hubLongitude = [101.37344116244806, 101.63982650389863, 101.68024844550233, 101.7901521759029, 101.57467295692778]

HubLocationArr = ["", "", "", "", ""]
for x in range (5):
    HubLocationArr[x] = ((hubLatitude[x], hubLongitude[x]))

"""
c1O = "Rawang"
c1D = "Bukit Jelutong"
customer1_Origin = ((3.3615395462207878, 101.56318183511695))
customer1_Destination = ((3.1000170516638885, 101.53071480907951))
distanceC1 = distance.distance(customer1_Origin,customer1_Destination).km, "KM"

c2O = "Subang Jaya"
c2D = "Puncak ALam"
customer2_Origin = ((3.049398375759954, 101.58546611160301))
customer2_Destination = ((3.227994355250716, 101.42730357605375))
distanceC2 = distance.distance(customer2_Origin,customer2_Destination).km, "KM"

c3O = "Ampang"
c3D = "Cyberjaya"
customer3_Origin = ((3.141855957281073, 101.76158583424586))
customer3_Destination = ((2.9188704151716256, 101.65251821655471))
distanceC3 = distance.distance(customer3_Origin,customer3_Destination).km, "KM"
"""

customerOrigin = ["Rawang", "Subang Jaya", "Ampang"]
originLatitude = [3.3615395462207878, 3.049398375759954, 3.141855957281073]
originLongitude = [101.56318183511695, 101.58546611160301, 101.76158583424586]

customerDestination = ["Bukit Jelutong", "Puncak Alam", "Cyberjaya"]
destinationLatitude = [3.1000170516638885, 3.227994355250716, 2.9188704151716256]
destinationLongitude = [101.53071480907951, 101.42730357605375, 101.65251821655471]

locationOrigin = ["", "", ""]
for x in range (3):
    locationOrigin[x] = ((originLatitude[x], originLongitude[x]))

locationDestination = ["", "", ""]
for x in range (3):
    locationDestination[x] = ((destinationLatitude[x], destinationLongitude[x]))

distanceOriToDes = ["", "", ""]
for x in range (3):
    distanceOriToDes[x] = distance.distance(locationOrigin[x],locationDestination[x]).km

totalDistanceC1 = ["", "", "", "", ""]
for x in range (5):
    totalDistanceC1[x] = (distance.distance(locationOrigin[0], HubLocationArr[x]).km + distance.distance(HubLocationArr[x], locationDestination[0]).km)

totalDistanceC2 = ["", "", "", "", ""]
for x in range (5):
    totalDistanceC2[x] = (distance.distance(locationOrigin[1], HubLocationArr[x]).km + distance.distance(HubLocationArr[x], locationDestination[1]).km)

totalDistanceC3 = ["", "", "", "", ""]
for x in range (5):
    totalDistanceC3[x] = (distance.distance(locationOrigin[2], HubLocationArr[x]).km + distance.distance(HubLocationArr[x], locationDestination[2]).km)

print('\n                           Hub: ', hubName)
print('Total distance Customer 1 (km): ', totalDistanceC1)
print('Total distance Customer 2 (km): ', totalDistanceC2)
print('Total distance Customer 3 (km): ', totalDistanceC3)

"""
locationHub1 = geolocator.geocode(hub1)
laloHub1 = ((locationHub1.latitude, locationHub1.longitude))

locationOriginC1 = geolocator.geocode(customerOrigin[2])
OC1 = ((locationOriginC1.latitude, locationOriginC1.longitude))

locationDestinationC1 = geolocator.geocode(customerDestination[2])
DC1 = ((locationDestinationC1.latitude, locationDestinationC1.longitude))

disC1Hub1 = distance.distance(OC1, laloHub1).km + distance.distance(laloHub1, DC1).km
test1 = distance.distance(locationOrigin[2], HubLocationArr[0]).km + distance.distance(HubLocationArr[0], locationDestination[2]).km

print(disC1Hub1)
print((test1))

print(laloHub1)
print(HubLocationArr[0])
"""

#location1 = geolocator.geocode(hub1)
#location2 = geolocator.geocode(hub2)
#location3 = geolocator.geocode(hub3)
#location4 = geolocator.geocode(hub4)
#location5 = geolocator.geocode(hub5)

#print(location1)
#print(location2)
#print(location3)
#print(location4)
#print(location5)

#print(location1.latitude)

#loc1 = ((l1.latitude, l1.longitude))
#loc2 = ((l2.latitude, l2.longitude))

#print(distance.distance(loc1,loc2).km, "kms")

# Q3

leastC1 = totalDistanceC1[0]
a = 0
leastC2 = totalDistanceC2[0]
b = 0
leastC3 = totalDistanceC3[0]
c = 0

for x in range(len(hubName)):
    if totalDistanceC1[x] < leastC1:
        leastC1 = totalDistanceC1[x]
        hubLeastC1 = hubName[x]
        a = x

    if totalDistanceC2[x] < leastC2:
        leastC2 = totalDistanceC2[x]
        hubLeastC2 = hubName[x]
        b = x
    
    if totalDistanceC3[x] < leastC3:
        leastC3 = totalDistanceC3[x]
        hubLeastC3 = hubName[x]
        c = x

print('\nLeast distance Customer 1: ', hubLeastC1, ' - ', leastC1, 'km') # , a)
print('Least distance Customer 2: ', hubLeastC2, ' - ', leastC2, 'km') # , b)
print('Least distance Customer 3: ', hubLeastC3, ' - ', leastC3, 'km') # , c)

# plotting the map

import gmplot

# Create the map plotter:
apikey = '' # (your API key here)
gmap = gmplot.GoogleMapPlotter(hubLatitude[0], hubLongitude[0], 14, apikey=apikey)

# Mark the Hubs:
for x in range(len(hubName)):
    gmap.marker(hubLatitude[x], hubLongitude[x], color='cornflowerblue')

# Highlight Customer's origins and destinations:
# color hash code: RED - #FF0000, GREEN - #00FF00, BLUE - #0000FF, YELLOW -	#FFFF00 
gmap.scatter(originLatitude, originLongitude, color='#FFFF00', size=400, marker=False)
gmap.scatter(destinationLatitude, destinationLongitude, color='#00FF00', size=400, marker=False)

# Draw a line for the distance of origin to hub to destination BEFORE using the algorithm
#oriLats , oriLngs = zip(*[
#    (originLatitude[0], originLongitude[0]),
#    (originLatitude[1], originLongitude[1]),
#    (originLatitude[2], originLongitude[2]),
#])

#gmap.plot(oriLats, oriLngs, 'cornflowerblue', edge_width = 3.0)

##gmap.plot(originLatitude, originLongitude, 'cornflowerblue', edge_width = 3.0)

#for y in range(len(customerOrigin)):
#    for x in range(len(hubName)):
#        beforeAlgoLats , beforeAlgoLngs = zip(*[
#            (originLatitude[y], originLongitude[y]),
#            (hubLatitude[x], hubLongitude[x]),
#            (destinationLatitude[y], destinationLongitude[y])
#        ])

#        gmap.plot(beforeAlgoLats, beforeAlgoLngs, 'cornflowerblue', edge_width = 3.0)

for x in range(len(hubName)):
        beforeAlgoLats1 , beforeAlgoLngs1 = zip(*[
            (originLatitude[0], originLongitude[0]),
            (hubLatitude[x], hubLongitude[x]),
            (destinationLatitude[0], destinationLongitude[0])
        ])

        gmap.plot(beforeAlgoLats1, beforeAlgoLngs1, 'cornflowerblue', edge_width = 3.0)

for x in range(len(hubName)):
        beforeAlgoLats2 , beforeAlgoLngs2 = zip(*[
            (originLatitude[1], originLongitude[1]),
            (hubLatitude[x], hubLongitude[x]),
            (destinationLatitude[1], destinationLongitude[1])
        ])

        gmap.plot(beforeAlgoLats2, beforeAlgoLngs2, 'red', edge_width = 3.0)
    
for x in range(len(hubName)):
        beforeAlgoLats3 , beforeAlgoLngs3 = zip(*[
            (originLatitude[2], originLongitude[2]),
            (hubLatitude[x], hubLongitude[x]),
            (destinationLatitude[2], destinationLongitude[2])
        ])

        gmap.plot(beforeAlgoLats3, beforeAlgoLngs3, 'yellow', edge_width = 3.0)

## Outline the Hub's area: (trial and error)
#hubArea = zip(*[
#    (hubLatitude[0], hubLongitude[0]),
#    (hubLatitude[1], hubLongitude[1]),
#    (hubLatitude[3], hubLongitude[3]),
#    (hubLatitude[2], hubLongitude[2]),
#    (hubLatitude[4], hubLongitude[4])
#])

#gmap.polygon(*hubArea, color='cornflowerblue', edge_width=10)
##

# Draw the map to an HTML file:
gmap.draw('map1.html')

# Draw a line for the distance of origin to hub to destination AFTER using the algorithm
afterAlgoLats1 , afterAlgoLngs1 = zip(*[
    (originLatitude[0], originLongitude[0]),
    (hubLatitude[a], hubLongitude[a]),
    (destinationLatitude[0], destinationLongitude[0])
])

gmap.plot(afterAlgoLats1, afterAlgoLngs1, 'cornflowerblue', edge_width = 3.0)


afterAlgoLats2 , afterAlgoLngs2 = zip(*[
    (originLatitude[1], originLongitude[1]),
    (hubLatitude[b], hubLongitude[b]),
    (destinationLatitude[1], destinationLongitude[1])
])

gmap.plot(afterAlgoLats2, afterAlgoLngs2, 'red', edge_width = 3.0)


afterAlgoLats3 , afterAlgoLngs3 = zip(*[
    (originLatitude[2], originLongitude[2]),
    (hubLatitude[c], hubLongitude[c]),
    (destinationLatitude[2], destinationLongitude[2])
])

gmap.plot(afterAlgoLats3, afterAlgoLngs3, 'yellow', edge_width = 3.0)

# Draw the map to an HTML file:
gmap.draw('map2.html')

print('\nCoordinates have been plotted to the map at: map1.html & map2.html')