#
# Copyright © 2018, "rupansh" <rupanshsekar@hotmail.com>
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
import urllib.request
from locationiq.geocoder import LocationIQ


countrylist = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
               "Australia", "Austria", "Azerbaijan", "The Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus",
               "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil",
               "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada",
               "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica",
               "Côte d’Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica",
               "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea",
               "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "The Gambia", "Georgia", "Germany", "Ghana",
               "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary",
               "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan",
               "Jordan", "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", "Kosovo", "Kuwait",
               "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania",
               "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
               "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia, Federated States of", "Moldova",
               "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru",
               "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan",
               "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
               "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
               "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia",
               "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
               "Solomon Islands", "Somalia", "South Africa", "Spain", "Sri Lanka", "Sudan", "Sudan, South", "Suriname",
               "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo",
               "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
               "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu",
               "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
               ]

country = input("Enter the country ")

if country.casefold() in (count.casefold() for count in countrylist):
    # Map zoom
    print("Enter zoom level! 14 if you live in vatican city, 10-7 if you live in small Europe Countries",
          "6 for Average Europe country, 5 for average country, 4 for Large countries, 3 for Russia(or 2)")
    zoom = int(input())
    
    # locationIQ stuff
    geocoder = LocationIQ('insert yo token here')
    jsondata = geocoder.geocode(country)

    # use the lats and longs in json data dict
    latitude = jsondata[0]['lat']
    longitude = jsondata[0]['lon']

    # Googlemaps stuff
    url = "http://maps.googleapis.com/maps/api/staticmap?center={},{}&zoom={}&size=800x800&sensor=false&markers=color:blue%7Clabel:count%7C{},{}".format(latitude, longitude, zoom, latitude, longitude)  # static google maps api
    buffer = BytesIO(urllib.request.urlopen(url).read())  # idk how BytesIO works so I won't explain

    # Convert map to Image
    image = Image.open(buffer)
    image.show()

else:
    print("Country not found in list(Make sure to use full form of the name)")
