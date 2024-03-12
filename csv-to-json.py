import csv
import json
import time
import re


def csv_to_json(csvFilePath, jsonFilePath):
    # Read csv file
    with open(csvFilePath) as csvfile:
        # Load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvfile)

        # Regex expresion to match a special character present in the key list below
        regex = re.compile("[;]")

        try:
            # Gets the fisrt item from the csv dictionary
            x = next(csvReader)
            x = next(csvReader)
            # Gets the list of keys in the csv dictionary
            key = list(x.keys())[0]
            print(key)
        except:
            return print("The CSV file has no items")

        csvfile.seek(0)
        csvReader = csv.DictReader(csvfile)
        # Checks if the delimiter in the csv file is ';'
        if regex.search(key) is not None:
            # If the delimiter is ';', then we changes it in dictionary reader

            csvReader = csv.DictReader(csvfile, delimiter=";")

        # Convert each csv row into python dict
        data = [row for row in csvReader]

        # Definir la base del objeto
        response = define_backstage_json()
        for element in data:
            #print(element_to_entry(element))
            response["entries"].append(element_to_entry(element))

    # Convert python data Array to JSON String and write to file
    with open(jsonFilePath, "w", encoding="utf-8") as jsonfile:
        response = json.dumps(response, indent=4)
        jsonfile.write(response)


def define_backstage_json():
    return {
        "quadrants": [
            {"id": "techniques", "name": "Techniques"},
            {"id": "platforms", "name": "Platforms"},
            {"id": "language-and-frameworks", "name": "Language and frameworks"},
            {"id": "tools", "name": "Tools"},
        ],
        "rings": [
            {"id": "adopt", "name": "ADOPT", "color": "#93c47d"},
            {"id": "trial", "name": "TRIAL", "color": "#93d2c2"},
            {"id": "assess", "name": "ASSESS", "color": "#fbdb84"},
            {"id": "hold", "name": "HOLD", "color": "#efafa9"},
        ],
        "entries": [],
    }


def element_to_entry(element):
    return {
        "quadrant": element["quadrant"],
        "description": element["description "],
        "key": element["name"],
        "id": element["name"],
        "title": element["name"],
        "timeline": [{"moved": 0, "ringId": element["ring"], "date": "2022-12-09"}],
    }


# Csv data file path
csvFilePath = r"radar.csv"
# Json data file path
jsonFilePath = r"radar.json"


start = time.perf_counter()
csv_to_json(csvFilePath, jsonFilePath)
finish = time.perf_counter()

print(f"Conversion completed successfully in {finish - start:0.4f} seconds")
