import os

if os.path.exists(r"C:\Users\serdar.yalcin\Documents\password.key"):
    os.remove(r"C:\Users\serdar.yalcin\Documents\password.key")
    print ("It has removed")
else:
    print ("It does not exist")
