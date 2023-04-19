import json # Needed to get image info dictionaries from json file
import os
import csv

# current path
current_path = os.path.dirname(os.path.abspath(__file__))

# Get images dictionary data from image_cruncher folder
# TO DO - make possible to enter file path / direct data input. now it only handles JSON files from same directory in which is the script.
path_to_json = f'{current_path}\\output.json'

# 1 . Load data from JSON file
# TO DO - make possible to enter file path / direct data input. now it only handles JSON files. - Pack this into function.\
# Make error handling for various exceptions - file not found, no data recieved ...

with open(path_to_json, 'r', encoding='UTF-8') as f:
    images_data = json.load(f)

# count pixels
greens = [int(data.get("green")) for image, data in images_data.items()]
count_greens = sum(greens)

blues = [int(data.get("blue")) for image, data in images_data.items()]
count_blues = sum(blues)

reds = [int(data.get("red")) for image, data in images_data.items()]
count_reds = sum(reds)

others = [int(data.get("other")) for image, data in images_data.items()]
count_others = sum(others)

all = greens + blues + reds + others
count_all = sum(all)

# Calculate percentage
greens_percentage = round(count_greens/count_all,4)
blues_percentage = round(count_blues/count_all,4)
reds_percentage = round(count_reds/count_all,4)
others_percentage = round(count_others/count_all,4)

# write data lines into CSV file
# TO DO - make possible to enter file path / direct data input. now it only handles JSON files. - Pack this into function
# Make error handling for various exceptions - invalid data, no data recieved, some other errors...all

# Make posible to save file to specific location.

with open(f'{current_path}\\dataID_analysis.csv', 'w', newline = "") as o:
    # Create a CSV writer object
    writer = csv.writer(o)  

    # write headings in ouput file
    writer.writerow(["Filename","Red","Green","Blue","Other"])

    # write all the data
    for image, data in images_data.items():
        colours = [str(data.get(colour)) for colour in data]
        colours.insert(0,image)
        writer.writerow(colours)

    # write pixel percentage
    writer.writerow(["Total", f'{str(reds_percentage*100)}%', f'{str(greens_percentage*100)}%', f'{str(blues_percentage*100)}%', f'{str(others_percentage*100)}%'])
