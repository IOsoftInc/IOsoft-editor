hopefuly = open("boot.log", "a")
hopefuly.close()
data = open("boot.log", "r").read()
if data == "":
    print("Welcome!")
else:
    print("I havent seen you since ", data)
