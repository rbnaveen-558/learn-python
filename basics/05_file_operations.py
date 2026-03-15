# Sample: Python File Operations

# Writing to a file
with open("sample.txt", "w") as f:
    f.write("Hello, file!\n")

# Reading from a file
with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:", content)

# Working with CSV
import csv
with open("sample.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["name", "age"])
    writer.writerow(["Alice", 30])

with open("sample.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print("CSV row:", row)

# Working with JSON
import json
data = {"name": "Bob", "age": 25}
with open("sample.json", "w") as jsonfile:
    json.dump(data, jsonfile)

with open("sample.json", "r") as j:
    loaded = json.load(j)
    print("JSON data:", loaded)
