name = input("Enter your name:")
age = input("Enter your age:")
address = input("Enter your address:")
if not age.isdigit() :
    print("Error,\nage type isn't valid.")
    exit()
if address.isdigit():
    print("Error,\naddress type isn't valid.")
    exit()
if name == ("") or name == None:
    print("Error,\nname type isn't valid.")
    exit()
if age == ("") or age == None:
    print("Error,\nage type isn't valid.")
    exit()
if address == ("") or address == None:
    print("Error,/naddress name isn't valid")
    exit()
print ("Hello Mr/Ms",name,"age",age,"located in",address ,"\nthanks for being one of our community,    Enjoy")
