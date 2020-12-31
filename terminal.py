import os
import easygui as g

choice = 0

def dictionary(dict1):
    global string1
    for eachItem in dict1.items():
        string1 += str(eachItem[0]) + ': ' + str(eachItem[1]) + '\n'

def check_close():
    global choice
    choice = int(g.buttonbox(msg=string1, title='Terminal', choices=('0', '1','2','3', '4','5','9'), image=None, images=None, default_choice=None, cancel_choice=None, callback=None, run=True))

def get_working_directory():
    g.msgbox(msg = 'The current working directory is: ' + os.getcwd(),title='terminal')

def thanks():
    checker = g.buttonbox(msg='Are you sure to exit?', title='Terminal', choices=('Yes', 'No'), image=None, images=None, default_choice=None, cancel_choice=None, callback=None, run=True)
    if checker == 'Yes':
        g.msgbox(msg = 'Thanks for using, byebye!',title='terminal')
        return 1
    else:
        return -1

def mkdir_new(string1):
        # add ,ore functions
    checker = g.buttonbox(msg=string1, title='terminal', choices=('make new direcory', 'make new direcories', 'cancel'), image=None, images=None, default_choice=None, cancel_choice=None, callback=None, run=True)
    if checker == 'make new direcory' or checker == 'make new direcories':            
        enter = g.enterbox(msg='Enter the new file name.', title='terminal', default=os.getcwd(), strip=True, image=None, root=None)
        try:
            if checker == 'make new direcory':
                os.mkdir(enter)
            else:
                os.makedirs(enter)
            g.msgbox(msg = 'the folder create successful!',title = 'terminal')
        except OSError:
            g.msgbox(msg = 'the folder exists or enter a wrong director!',title = 'terminal')
        except TypeError:
            g.msgbox(msg = 'the insert can not be empty!',title = 'terminal')

def list_to_str(list_1):
    string2 = ''
    for each_list in list_1:
        string2 += each_list + '\n'
    return string2

def list_files():
    enter = g.enterbox(msg='Enter the specific direcotry.', title='terminal', default=os.getcwd(), strip=True, image=None, root=None)
    try:
        list1 = os.listdir(enter)
        string1 = list_to_str(list1)
        mkdir_new(string1)
    except OSError:
        g.msgbox(msg = 'the directory not exists or empty enter!',title='terminal')
        return 1
    except TypeError:
        return -1 

def folder_remove():
    enter = g.enterbox(msg=list_to_str(os.listdir(os.getcwd())), title='terminal', default=os.getcwd(), strip=True, image=None, root=None)
    try:
        os.rmdir(enter)
        return 1
    except PermissionError:
        return -1

def file_remove():
    enter = g.enterbox(msg=list_to_str(os.listdir(os.getcwd())), title='terminal', default=os.getcwd(), strip=True, image=None, root=None)
    try:
        os.remove(enter)
        return 1
    except PermissionError:
        return -1
    except TypeError:
        return -2    
    

while True:
    string1 = ''
    dict1 = {0:'get the current working directory',
    1:'change the working directory',
    2:'list the files in the specific directory',
    3:'make new directory',
    4:'remove folder',
    5:'remove file',
    9:'exit'}
    dictionary(dict1)

    try:
        check_close()
    except TypeError:
            yes_or_no = thanks()
            if yes_or_no == 1:
                break
            else:
                continue

    if choice == 0:
        get_working_directory()

    elif choice == 1:
        enter = g.enterbox(msg='Enter the direcotry.', title='terminal', default=os.getcwd(), strip=True, image=None, root=None)

        try:
            os.chdir(enter)
        except OSError:
            g.msgbox(msg = 'the directory not exists or empty enter!',title='terminal')
        except TypeError:
            continue          

    elif choice == 2:
        checker = list_files()
        if checker == -1:
            continue

    elif choice == 3:
        try:
            mkdir_new(string1)
        except OSError:
            continue

    elif choice == 4:
        check = folder_remove()
        if check == -1:
            g.msgbox(msg = 'no permission!',title='terminal')
        else:
            g.msgbox(msg = 'successful remove!',title='terminal')

    elif choice == 5:
        check = file_remove()
        if check == -1:
            g.msgbox(msg = 'no permission!',title='terminal')
        elif check == -2:
            continue
        else:
            g.msgbox(msg = 'successful remove!',title='terminal')

    elif choice == 9:
        yes_or_no = thanks()
        if yes_or_no == 1:
            break
        else:
            continue



        