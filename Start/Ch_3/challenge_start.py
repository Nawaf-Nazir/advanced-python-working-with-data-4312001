# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

def getsig(x):
    sig = x["properties"]["sig"]
    return 0 if sig is None else sig

def bytime(x):
    date = datetime.date.fromtimestamp(int(x["properties"]["time"]/1000))
    return date

# Filter the data by quakes that are larger than 5 magnitude
largequakes = sorted(data["features"], key = getsig, reverse = True)
largequakes = largequakes[:40]
largequakes.sort(key = bytime, reverse=True)
#print(largequakes)
# TODO: Create the header and row structures for the data
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
header = ["Magnitude", "Place", "Felt Reports", "Date", "Google Map link"]
rows =[]

# TODO: populate the rows with the resulting quake data
for quake in largequakes:
    thedate = datetime.date.fromtimestamp(int(quake["properties"]["time"]/1000))
    lat = quake["geometry"]["coordinates"][1]
    long = quake["geometry"]["coordinates"][0]
    gmaplink = f"https://www.google.com/maps/search/?api=1&query={lat}%2C{long}"
    rows.append([quake["properties"]["mag"],
                quake["properties"]["place"],
                quake["properties"]["felt"],
                thedate,
                gmaplink]
                )
# TODO: write the results to the CSV file
with open("significantevents.csv", 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)