import re, json
olgas_dict = {}

with open('./dir2json.txt', 'r+') as data:
    for line in data:
        list_of_2 = line.split("--")
        seq_num, img_title= list_of_2[0].split("_")
        img_title_list = img_title.split("-")
        dfi_img_number = ''.join(re.findall('\d+', list_of_2[1]))
        author = "Peter Elfelt"
        olgas_dict[dfi_img_number] = [seq_num, img_title_list, author, line]

print olgas_dict
