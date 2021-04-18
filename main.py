import f1pystats as f1stats
import gspread
from gspread_formatting import *
from oauth2client.service_account import ServiceAccountCredentials
import json
import sys

import constants

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

players = 4

def update_sheet(year):
    sheet = client.open("F1 2021 Predictions").sheet1
    if len(sys.argv) > 1 and len(sys.argv) <= 3:
        r = "last"
        if len(sys.argv) == 3:
            r = sys.argv[2]
        for it in sys.argv[1]:
            if it == "u":
                print("Updating podium for round " + r)
                update_results(sheet, year, r)
            elif it == "c":
                print("Checking bets for round " + r)
                check_results(sheet, year, r)
            elif it == "i":
                print("Creating/Updating countries")
                update_countries(sheet, year)
    else:
        print("Error: 1 argument needed")
        print(" - u: Update poduium")
        print(" - c: Check bets")
        print(" - i: Update counties names")

def update_countries(sheet, year):
    data = f1stats.get(str(year))
    circuits = data["RaceTable"]["Races"]
    total = int(data["total"])
    for i in range(total):
        name = circuits[i]["Circuit"]["Location"]["country"]
        sheet.update_cell(1, i+2, name)
        print("Updated: " + name)

def update_results(sheet, year, rnd="last"):
    data = f1stats.get(str(year) + " " + str(rnd) + " results")
    if rnd == "last":
        rnd = int(data["RaceTable"]["round"])
    else:
        rnd = int(rnd)
    for i in range(3):
        driver = data["RaceTable"]["Races"][0]["Results"][i]["Driver"]
        name = driver["familyName"]
        id = driver["driverId"]
        c_update_cell(sheet, 31+i, rnd+1, name, constants.drivers_color[id][0], constants.drivers_color[id][1])
        print("Updating: " + name + " on " + str(i) + "place")
    id = get_fl(year, rnd)
    name = constants.drivers_name[id]
    c_update_cell(sheet, 34, rnd+1, name, constants.drivers_color[id][0], constants.drivers_color[id][1])

def check_results(sheet, year, rnd="last"):
    global players
    data = f1stats.get(str(year) + " " + str(rnd) + " results")
    if rnd == "last":
        rnd = int(data["RaceTable"]["round"])
    else:
        rnd = int(rnd)
    
    podium = get_podium(year, rnd)
    fl_name = get_fl(year, rnd)

    for p in range(players):
        score = 0
        for i in range(0, 3):
            x = 3+(p*7)+i
            y = rnd+1
            val = sheet.cell(x, y).value
            col = None
            if val.lower() == constants.drivers_name[podium[i]].lower():
                col = constants.color_right
                score += 1
            else:
                col = constants.color_wrong
            c_update_cell(sheet, x, y, val, col)
        x = 3+(p*7)+3
        y = rnd+1
        val = sheet.cell(x, y).value
        if val.lower() == constants.drivers_name[fl_name].lower():
            col = constants.color_right
            score += 1
        else:
            col = constants.color_wrong
        c_update_cell(sheet, x, y, val, col)
        curr_score = int(sheet.cell(2+p*7, 4).value)
        c_update_cell(sheet, 2+p*7, 4, str(curr_score+score))

def get_podium(year, rnd="last"):
    data = f1stats.get(str(year) + " " + str(rnd) + " results")
    podium = []
    for i in range(3):
        driver = data["RaceTable"]["Races"][0]["Results"][i]["Driver"]
        name = driver["driverId"]
        podium.append(name)
    return podium

def get_fl(year, rnd="last"):
    data = f1stats.get(str(year) + " " + str(rnd) + " results")
    fl_id = "No Name"
    fl_millis = 9999999999999999999
    drivers = data["RaceTable"]["Races"][0]["Results"]
    for i in range(len(drivers)):
        if("FastestLap" not in drivers[i].keys()):
            continue
        time = min_to_millis(drivers[i]["FastestLap"]["Time"]["time"])
        if time < fl_millis:
            fl_id = drivers[i]["Driver"]["driverId"]
            fl_millis = time
    return fl_id

def min_to_millis(time):
    t = time.split(":")
    m = int(t[0])*60000
    t = t[1].split(".")
    s = int(t[0])*1000
    mi = int(t[1])

    return m+s+mi

def c_update_cell(sheet, x, y, name, cb=Color(1, 1, 1), ct=Color(0, 0, 0)):
    sheet.update_cell(x, y, name)
    fmt = CellFormat(backgroundColor=cb, textFormat=textFormat(foregroundColor=ct))
    format_cell_range(sheet, gspread.utils.rowcol_to_a1(x, y), fmt)

update_sheet(2021)
