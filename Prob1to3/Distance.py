import geopy
from geopy.geocoders import Nominatim
from geopy import distance

import array as arr

geolocator = Nominatim(user_agent="geoapiExercises")

hubName = ["Port Klang", "Petaling Jaya", "Batu Caves", "Kajang", "Sungai Buloh"]

hubLatitude = [3.0319924887507144, 3.112924170027219, 3.265154613796736, 2.9441205329488325, 3.2127230893650065]
hubLongitude = [101.37344116244806, 101.63982650389863, 101.68024844550233, 101.7901521759029, 101.57467295692778]

HubLocationArr = ["", "", "", "", ""]
for x in range (5):
    HubLocationArr[x] = ((hubLatitude[x], hubLongitude[x]))

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

hubIndexC1=[0,1,2,3,4]
hubIndexC2=[0,1,2,3,4]
hubIndexC3=[0,1,2,3,4]
def selectionSortTotalDistance(array, size, hubIndex):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i


        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        (hubIndex[step], hubIndex[min_idx]) = (hubIndex[min_idx], hubIndex[step])

selectionSortTotalDistance(totalDistanceC1, len(totalDistanceC1), hubIndexC1)
selectionSortTotalDistance(totalDistanceC2, len(totalDistanceC2), hubIndexC2)
selectionSortTotalDistance(totalDistanceC3, len(totalDistanceC3), hubIndexC3)

print('\nLeast distance Customer 1: ', hubName[hubIndexC1[0]], ' - ', totalDistanceC1[0], 'km')
print('Least distance Customer 2: ', hubName[hubIndexC2[0]], ' - ', totalDistanceC2[0], 'km')
print('Least distance Customer 3: ', hubName[hubIndexC3[0]], ' - ', totalDistanceC3[0], 'km')

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

for x in range(len(hubName)):
    beforeAlgoLats1, beforeAlgoLngs1 = zip(*[
        (originLatitude[0], originLongitude[0]),
        (hubLatitude[x], hubLongitude[x]),
        (destinationLatitude[0], destinationLongitude[0])
    ])

    gmap.plot(beforeAlgoLats1, beforeAlgoLngs1, 'cornflowerblue', edge_width=3.0)

for x in range(len(hubName)):
    beforeAlgoLats2, beforeAlgoLngs2 = zip(*[
        (originLatitude[1], originLongitude[1]),
        (hubLatitude[x], hubLongitude[x]),
        (destinationLatitude[1], destinationLongitude[1])
    ])

    gmap.plot(beforeAlgoLats2, beforeAlgoLngs2, 'red', edge_width=3.0)

for x in range(len(hubName)):
    beforeAlgoLats3, beforeAlgoLngs3 = zip(*[
        (originLatitude[2], originLongitude[2]),
        (hubLatitude[x], hubLongitude[x]),
        (destinationLatitude[2], destinationLongitude[2])
    ])

    gmap.plot(beforeAlgoLats3, beforeAlgoLngs3, 'yellow', edge_width=3.0)

# Draw the map to an HTML file:
gmap.draw('map1.html')

# Draw a line for the distance of origin to hub to destination AFTER using the algorithm
afterAlgoLats1 , afterAlgoLngs1 = zip(*[
    (originLatitude[0], originLongitude[0]),
    (hubLatitude[hubIndexC1[0]], hubLongitude[hubIndexC1[0]]),
    (destinationLatitude[0], destinationLongitude[0])
])

gmap.plot(afterAlgoLats1, afterAlgoLngs1, 'cornflowerblue', edge_width = 3.0)


afterAlgoLats2 , afterAlgoLngs2 = zip(*[
    (originLatitude[1], originLongitude[1]),
    (hubLatitude[hubIndexC2[0]], hubLongitude[hubIndexC2[0]]),
    (destinationLatitude[1], destinationLongitude[1])
])

gmap.plot(afterAlgoLats2, afterAlgoLngs2, 'red', edge_width = 3.0)


afterAlgoLats3 , afterAlgoLngs3 = zip(*[
    (originLatitude[2], originLongitude[2]),
    (hubLatitude[hubIndexC3[0]], hubLongitude[hubIndexC3[0]]),
    (destinationLatitude[2], destinationLongitude[2])
])

gmap.plot(afterAlgoLats3, afterAlgoLngs3, 'yellow', edge_width = 3.0)

# Draw the map to an HTML file:
gmap.draw('map2.html')

print('\nCoordinates have been plotted to the map at: map1.html & map2.html')