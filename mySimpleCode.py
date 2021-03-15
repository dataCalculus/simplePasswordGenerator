#33 - 126 ascii table
#possible valid character range

import random

password = ""

def generatePasswd():
    ascii_int = random.randint(33,126)
    ascii_char = chr(ascii_int)
    return ascii_char

passwordList=[]
for i in range(4):
    passwordList.append(generatePasswd())
print(passwordList)

for i in range(len(passwordList)):
    password=password+passwordList[i]
print("password is : {}".format(password))