"""Import all file names in a specific dir and store it as JSON file """
import os, json

with open("./dir2json.txt", 'w') as img_file:
    for file_in_dir in os.walk("./stereoviews_by_peter_elfelt"):
        for filename in file_in_dir:
            json.dump(filename, img_file, indent=4)
