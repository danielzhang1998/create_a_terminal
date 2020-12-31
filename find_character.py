import os

def search_in_file(file_name, search_character):
    character_len = len(search_character)
    file_base_name = os.path.basename(file_name)
    dir_name = os.path.dirname(file_name)
    file = open(file_name, 'r') # 文件打开

    count = 0
    for each_line in file:
        count += 1
        array_store = []
        pointer = 0
        result = -1

        while pointer <= character_len: # 当未达到当前行的末尾时，尝试搜寻下一个
            try:
                result = each_line.index(search_character, pointer)
            except ValueError:  # 当该行无匹配项时退出循环，进入下一行
                break
            if result >= 0:
                pointer = result + 1    # 指针后移
                array_store.append([result, result + character_len])
            else:
                break
        if len(array_store):    # 当列表不为空时，打印结果
            print("'" + search_character + '\' exists at line ' + str(count) + ', position: ', end='')
            for each in range(len(array_store)):
                print(array_store[each], end = ' ')
            print('in file: ' + file_base_name + 'and the address is: ' + dir_name)
    file.close()

def search_files(address, search_character):
    os.chdir(address)
    all_files = os.walk(address)
    txt_files = []
    list1 = list(all_files)
    count_each_file = 0
    for each_file in list1:
        for each_item in each_file:
            for every in each_item:
                if every.split('.')[-1] == 'txt':   
                    txt_files.append(list1[count_each_file][0] + '/' + every)
        count_each_file += 1

    for each in txt_files:
        search_in_file(each, search_character)

address = input('enter the files address:\n')
search_character = input('the character want to search:\n')
search_files(address, search_character)
