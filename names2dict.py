import re
olgas_dict = {}


with open("./dir2json.txt", 'r+') as data:
    for line in data:
        list_of_2 = line.split("_")
        title = list_of_2[0].split("-")
        img_number = ''.join(re.findall('\d+', list_of_2[1]))
        olgas_dict[img_number] = title
print(olgas_dict)