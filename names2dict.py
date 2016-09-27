import string
olgas_dict = {}

with open('./dir2json.txt', 'r+') as data:
    for line in data:
        list_of_2 = line.split("--")
        seq_num, img_title = list_of_2[0].split("_")
        img_title_list = img_title.split("-")
        #dfi_img_number = ''.join(re.findall('\d+', list_of_2[1]))
        dfi_img_number = list_of_2[1].translate(list_of_2[1], string.digits)
        int_seq = seq_num.translate(seq_num, string.digits)
        olgas_dict[dfi_img_number] = [seq_num, img_title_list, "Peter Elfelt", line]

with open("amost_db.txt", 'w') as txt_file:
     txt_file.write(str(olgas_dict))
