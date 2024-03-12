import pandas as pd
import time

def csv_to_json_pnd(csvFilePath, jsonFilePath):
    # Read csv file
    df = pd.read_csv (csvFilePath)
    print(df)

# Csv data file path
csvFilePath = r"radar.csv"
# Json data file path
jsonFilePath = r"radar_pnd.json"


start = time.perf_counter()
csv_to_json_pnd(csvFilePath, jsonFilePath)
finish = time.perf_counter()

print(f"Conversion completed successfully in {finish - start:0.4f} seconds")