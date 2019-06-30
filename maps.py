#
# Copyright © 2019, "rupansh" <rupanshsekar@hotmail.com>
#
# This software is licensed under the terms of the GNU General Public
# License version 3, as published by the Free Software Foundation, and
# may be copied, distributed, and modified under those terms.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# Please maintain this if you use this script or any part of it


from io import BytesIO
from PIL import Image
import requests
from locationiq.geocoder import LocationIQ, LocationIqNoPlacesFound

# Constants
KEY = 'ENTER LOCATIONIQ TOKEN HERE'
SIZE = '800x800'

place = input("Enter the place ")

if place:
    # Map zoom
    zoom = int(input("Enter zoom level: "))

    # locationIQ stuff
    geocoder = LocationIQ(KEY)
    try:
        jsondata = geocoder.geocode(place)
    except LocationIqNoPlacesFound:
        print("Couldn't find the entered location!")
        exit(1)

    # use the lats and longs in json data dict
    latitude = jsondata[0]['lat']
    longitude = jsondata[0]['lon']

    static_map = f"https://maps.locationiq.com/v2/staticmap?key={KEY}&markers={latitude},{longitude}|icon:large-red-cutout;&zoom={zoom}&size={SIZE}"

    # fetch map from static locationiq api
    map = requests.get(static_map)

    # Convert map to byte data
    buf = BytesIO()
    buf.name = "map.png"
    for chunk in map.iter_content(chunk_size=128):
        buf.write(chunk)

    buf.seek(0)

    # Convert map's Bytedata to Image
    image = Image.open(buf)
    image.show()

else:
    print("Input a place lol!")
