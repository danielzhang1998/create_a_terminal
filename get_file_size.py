import os

files = os.listdir('.')

dict1 = {}

for each_file in files:
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        dict1[each_file] = file_size

for each_item in dict1.items():
    print(each_item[0] + '\t' + str(each_item[1]) + 'Bytes')
