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

    # Convert python data Array to JSON String and write to file
    with open(jsonFilePath, "w", encoding="utf-8") as jsonfile:
        jsonString = json.dumps(data, indent=4)
        jsonfile.write(jsonString)


# Csv data file path
csvFilePath = r"radar.csv"
# Json data file path
jsonFilePath = r"radar.json"


start = time.perf_counter()
csv_to_json(csvFilePath, jsonFilePath)
finish = time.perf_counter()

print(f"Conversion completed successfully in {finish - start:0.4f} seconds")
