"""Import all file names in a specific dir and store it as JSON file """
import os, json

with open("./dir2json.txt", 'wr+') as img_file:
    for root, dirs, file_in_dir in os.walk("stereoviews_by_peter_elfelt/"):
        for filename in file_in_dir:
            json.dump(filename, img_file, indent=2)
            img_file.write('\n')
