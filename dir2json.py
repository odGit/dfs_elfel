"""Import all file names in a specific dir and store it as JSON file """
import os, json

with open("./dir2json.txt", 'w') as img_file:
    for root, dirs, file_in_dir in os.walk("stereoviews_by_peter_elfelt/", topdown=True):
        olga = [filename for filename in file_in_dir if not filename[0] == (".")]
        for filename in olga:
            json.dump(filename, img_file, indent=2)
            img_file.write('\n')
