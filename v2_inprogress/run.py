import os,sys,datetime
#FUNCTIONTS
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
def your_path(path):
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
def last_mod(file):
    import os
    with os.scandir(path):
        from datetime import datetime as dt
        last_modified = os.stat(file).st_mtime
        last_modified = dt.fromtimestamp(last_modified)
        return last_modified


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

            #PATH

try:

    path = input("Enter Path:\n >")
    your_path(path)

except ValueError:
    print("SORRY try again")
    sys.exit()


            #date
date=take_date()

print(path,date)
