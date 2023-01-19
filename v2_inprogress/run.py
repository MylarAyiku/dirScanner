import os,sys,datetime
from datetime import datetime
#FUNCTIONTS
#dir details

#op_1

def list_files():
    path = take_path()
    files = []
    print("Listing all files...")

    for root, dirs, files in os.walk(path):

        for filename in files:
            print(os.path.join(root, filename))

        return files

#op_4
def directory_details():
    directory=take_path()
    print("Directory: {}".format(directory))

    for filename in os.listdir(directory):
        print("Filename: {}".format(filename))
        # size
        size = os.stat(directory + "/" + filename).st_size
        act_size = size_format(size)
        print("Size: {}".format(act_size))

        print("Type: {}".format(os.stat(directory + "/" + filename).st_mode))
        # last mod
        mod = os.stat(directory + "/" + filename).st_mtime
        lst_mod = datetime.fromtimestamp(mod)
        print("Last modified: {}".format(lst_mod))
        print("\n")

def user_choice(ans):
    if ans==1:
        list_files()
    elif ans==2:
        directory_details()
        pass
    elif ans==3:
#         copy_files(path=directory,file):
        pass
    elif ans==4:
        # remove_files():
         pass
    elif ans==5:
        sys.exit()
    else:
        print("Please Try again .\nTry integers")


#OPTIONS
def what_else():
    print("Would you like to do close or continue ?")
    try:
        option = int(input("1.Continue \n0.Cancel \n>"))
        if option >= 0 and option < 2:
            return option
        else:
            print("Sorry ...Wrong input  \nTry either option 0 or 1 ")
            what_else()


    except:
        print("Wrong input ")
        sys.exit()
def prompt_action():

    #print("What would you like to do with the files in {}?".format(directory))
    print("What would you like to do ?")
    print("Options:")

    print("1. Print only files in a directory \n2. List everything in a directory \n3. Copy the files \n4. Remove the files  \n5. Exit")
    print(" \n")
    choice = int(input("Enter choice :"))
    return user_choice(choice)


#date
def is_date(y,m,d):###WORKING
    try:
        date=datetime.datetime(y,m,d)
        if date:
            return True
        else:
            return False
    except ValueError:
        return False


def check_timeline(year, month, day):
    your_date = datetime.datetime(year, month, day)

    now = datetime.datetime.now()
    today = (int(now.year), int(now.month), int(now.day))
    in_date = (year, month, day)
    if in_date > today:
        return False
    elif in_date == today:
        return your_date

    else:

        return your_date



def take_date():
    year=int(input('Enter year :'))
    month=int(input('Enter month :'))
    day=int(input('Enter Day :'))
    while not is_date(year,month,day):
        print('Please check the date well...')
        print("Try again..")
        year=int(input('Enter year :'))
        month=int(input('Enter month :'))
        day=int(input('Enter Day :'))
    ans=check_timeline(year,month,day)
    if ans ==False:
        print('Please check the date well')
        take_date()
    else:
        return ans


#....................................................................................

#path
def take_path():
    path = input("Enter Path:\n >")
    right = os.path.isdir(path)
    if not right:
        while not right:
            print("## Please check your path and try again ##\n try c:\\file\\name or /home/usr/directory  ")
            path = input("Enter Path:\n >")
            right = os.path.isdir(path)
    else:

        return path
#---------------------------------------------------------------
# FILE

# last modified
# def last_mod(file):
#     import os
#     with os.scandir(path):
#         from datetime import datetime as dt
#         last_modified = os.stat(file).st_mtime
#         last_modified = dt.fromtimestamp(last_modified)
#         return last_modified


# File size
def size_format(b):
    if b < 1000:
        return '%i' % b + 'B'
    elif 1000 <= b < 1000000:
        return '%.1f' % float(b / 1000) + 'KB'
    elif 1000000 <= b < 1000000000:
        return '%.1f' % float(b / 1000000) + 'MB'
    elif 1000000000 <= b < 1000000000000:
        return '%.1f' % float(b / 1000000000) + 'GB'
    elif 1000000000000 <= b:
        return '%.1f' % float(b / 1000000000000) + 'TB'






#*************************************************************************************8
#hard code

#first welcome
prompt_action()
option=what_else()
while option ==1:
    prompt_action()
    option = what_else()
print("Thank you")

