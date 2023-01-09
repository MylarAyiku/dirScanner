import os
import sys
import time


# declared functions
# correctDate
def correct(y, m, d):
    from datetime import datetime
    today_date = datetime.now()
    in_date = datetime(y, m, d)
    correct_stats = in_date <= today_date
    if correct_stats:
        return 1
    else:
        return 0


# About

def about(file):
    with os.scandir(path) as dirs:
        for file in dirs:
            print(file.name)
            print("CREATED: %s" % time.ctime(os.path.getctime(file)))
            file_size = os.stat(file).st_size
            print("SIZE: ", size_format(file_size))
            print("--------------------------")


# size
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


# check particular error with date
def check(type):
    if type == int(type) | len(type) < 5:
        print("sharp")
    else:
        print("")
        print(f"Please check your {type} well.")

        sys.exit()


# date modified

def last_mod(file):
    import os
    with os.scandir(path):
        from datetime import datetime as dt
        last_modified = os.stat(file).st_mtime
        last_modified = dt.fromtimestamp(last_modified)
        return last_modified


# main ##################


try:

    input1 = input("Enter Directory example:C:\File\path \n >")
    reply = os.path.isdir(input1)

    while not reply:
        print("Check your path well")
        input1 = input("Enter Directory example:C:\File\path \n >")
        reply = os.path.isdir(input1)
        if not reply:

            continue
        else:
            break





except:
    print("Please check your Path.")
    print("Are you sure you are typing a path ?")
    print("Try something like this C:\File\path ")
    sys.exit()




else:
    print(f"{input1}")
    print("\n")

    ## Date

    from datetime import datetime, date

    print("##### indicate the Date you want to be scanned against ####")
    print("   ")
    try:

        from datetime import datetime, date

        year = input("Enter Year:")
        month = input("Enter month:")
        day = input("Enter day:")
        today = datetime.now()
        year = int(year)
        month = int(month)
        day = int(day)

        if int(month) >= 13 or len(str(year)) >= 5 or int(day) >= 32:
            while True:
                print("Please check date well")
                year = int(input("Enter Year:"))
                month = int(input("Enter month:"))
                day = int(input("Enter Day:"))
                if month >= 13 or len(str(year)) >= 5 or day >= 32:
                    continue
                else:
                    break
        inDate = datetime(year, month, day)
        ans = correct(year, month, day)

        if ans == 0:
            while True:
                print("Please check date well")
                year = int(input("Enter Year:"))
                month = int(input("Enter month:"))
                day = int(input("Enter Day:"))
                if month >= 13 or len(str(year)) >= 5 or day >= 32:
                    continue
                else:
                    break
        elif ans == 1:
            print("Scanning...")

    except:
        print("Sorry!!!")
        print("Are you serious at all")
        sys.exit()
    else:

        path = input1

        print(path)
        print(inDate)

        ################PROCESS#############
        print("Loading:")

        animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        # animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
        # "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

        # Grouped List of Files
        list1 = []
        list2 = []

        with os.scandir(path) as dirs:
            for files in dirs:
                if last_mod(files) < inDate:
                    list1.append(files.name)
                else:
                    list2.append(files.name)

        if len(list1) == 0:
            print(f"There are no files dated below {inDate} ")
            print('\n')

        else:
            print("==================================================")
            print(f">>>>>>>> Files date below {inDate} <<<<<<<<<<<")
            print("==================================================")

            with os.scandir(path) as dirs:
                for doc in dirs:
                    if last_mod(doc) < inDate:
                        print(doc.name)
                        print("CREATED: %s" % time.ctime(os.path.getctime(doc)))
                        size = os.stat(doc).st_size
                        print("SIZE: ", size_format(size))
                        print("--------------------------")
            print("\n")
        if len(list2) == 0:
            print(f"There are no files dated Above {inDate} ")
            print('\n ')
        else:
            print("==================================================")
            print(f">>>>>>>> Files older than  {inDate}  <<<<<<<<<<<")
            print("==================================================")

            with os.scandir(path) as dirs:
                for doc in dirs:
                    if last_mod(doc) >= inDate:
                        print(doc.name)
                        print("CREATED: %s" % time.ctime(os.path.getctime(doc)))
                        size = os.stat(doc).st_size
                        print("SIZE: ", size_format(size))
                        print("--------------------------")
            print("\n")

input("DONE!...")
