#33 - 126 ascii table
#possible valid character range
import random
password = ""


def generatePasswd():
    ascii_int = random.randint(33,126)
    ascii_char = chr(ascii_int)
    return ascii_char

def generatePaswdList(count):
    passwordList=[]
    for i in range(count):
        passwordList.append(generatePasswd())
    return passwordList

def concatPassword(passwdList=[]):
    password=""
    for i in range(len(passwdList)):
        password=password+passwdList[i]
    return(password)

if __name__ == '__main__':
    lengthOfPasswd = int(input("Enter length of password you want ... :"))
    liste          = generatePaswdList(lengthOfPasswd)
    myPassword     = concatPassword(liste)
    print(myPassword)

