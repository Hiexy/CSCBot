import uuid
import csv

reader = csv.DictReader(open('sheet.csv', 'r', encoding="utf8"))

dict_list = []

for line in reader:
    dict_list.append(line)

new_list = []
for d in dict_list:
    new_dict = dict()
    new_dict['name'] = d['What is your Name?']
    new_dict['email'] = d['Email address']
    new_dict['ID'] = d['What is your Student ID?']
    new_dict['class'] = d['What level of training would you like to receive?'].split()[0]
    new_dict['token'] = str(uuid.uuid4())
    new_list.append(new_dict)


keys = new_list[0].keys()

with open('final.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(new_list)
