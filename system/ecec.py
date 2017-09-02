import datetime
masterboot = open("boot.log", "a")
add = str(datetime.datetime.now())
masterboot.write(add)
masterboot.write("\n")
masterboot.close()
