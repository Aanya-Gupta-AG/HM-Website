## Part 2 (all parts compiled)

## Cleaning the CSV

import csv

off_rows = []

with open('LAB2_AG.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        if "" not in row:  
            off_rows.append(row)

with open('OFF_LAB2_AG.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(off_rows)

## Endpoint 0

import requests

def create_api_key(username):
    response = requests.post(
        "https://ifenghm.pythonanywhere.com/create_api_key",
        headers={"Content-Type": "application/json"},
        json={"username": username}
    )
    print(response.text)  

create_api_key("aanya1_gupta1")

## Endpoint 1 

file_path = "OFF_LAB2_AG.csv"
columns = ["ref_pop", "access_to_elec", "prim_schl_enrollment", "prim_complete_rate", "fert_rate"]

my_data = {col: [] for col in columns}

with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        for col in columns:
            value = row[col]
            try:
                my_data[col].append(int(float(value)))  
            except ValueError:
                my_data[col].append(value)  

response = requests.post(
    "https://ifenghm.pythonanywhere.com/upload",
    headers={
        "Content-Type": "application/json",
        "apikey": api_key
    },
    json=my_data
)

print(response.json())

## Endpoint 2

params = {
    "independent": "ref_pop",  
    "dependent": "access_to_elec",  
    "id": "83ca9327-6719-427b-9f18-49eefa157d1c"
}

response = requests.get(
    "https://ifenghm.pythonanywhere.com/analyze",
    headers={"apikey": api_key},
    params=params
)

print(response.json())
