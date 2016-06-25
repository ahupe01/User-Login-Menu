import os
import base64
import hashlib

status = 0
userDict = {}

def read_in_file():
    
    with open ('password.txt') as passWordFile:
        
        line = passWordFile.read()
        
        user = line.strip().split('\n')

        for each in user:
            (user,userSalt64, passHash)=each.split(':')
            userDict[user] = [userSalt64, passHash]

    passWordFile.close()


def displayMenu():
    
    global status
    
    while(True):
        
        print("1) Add Username/Password")
        
        print("2) Change Password")
        
        print("3) Delete Username/Password")
        
        print("4) Exit Menu")
        
        
        
        status = raw_input("\nEnter choice: ")
        status = int(status)
        if (status < 1 or status > 4):           
            print("\nNot a valid entry\n")
            displayMenu();
        
        elif status == 1:

            newUser();

        elif status == 2:
    
            changePass();

        elif status == 3:
    
            deleteUser();

        elif status == 4:
            Exit();


def newUser():

    
    userName = raw_input("Create username: ")
    
    if userDict.get(userName):
        
        print "\nUsername already exists!\n"
    
    else:

        userSalt = os.urandom(6)
        userSalt64 = base64.b64encode(userSalt)
        passWord = raw_input("\nCreate password: ")
        
        hashObj=hashlib.sha256()
        hashObj.update(passWord)
        hashObj.update(userSalt)
        hashDigest=hashObj.digest()
        passHash = base64.b64encode(hashDigest)
        
        userDict[userName]=[userSalt64, passHash]
        
        print("\nAccount created!\n")

def changePass():
    
    userName = raw_input("\nEnter username: ")
    
    if userDict.get(userName):
        userSalt64 = (userDict[userName][0])
        userSalt = base64.b64decode(userSalt64)
        
        passTry = raw_input("\nEnter password: ")
        
        hashObj=hashlib.sha256()
        hashObj.update(passTry)
        hashObj.update(userSalt)
        hashDigest=hashObj.digest()
        passHash = base64.b64encode(hashDigest)
        userSalt64 = base64.b64encode(userSalt)
        
        
        if passHash == (userDict[userName][1]):
            passWord = raw_input("\nEnter new password: ")
            hashObj=hashlib.sha256()
            hashObj.update(passWord)
            hashObj.update(userSalt)
            hashDigest=hashObj.digest()
            passHash = base64.b64encode(hashDigest)
            
            
            userDict[userName]=[userSalt64, passHash]
    
            print("\nPassword has been changed\n")
        else:
            print("\nIncorrect login information\n")
    else:
        print("\nUsername not in database")

def deleteUser():
    
    userName = raw_input("\nEnter username: ")
    if userDict.get(userName):
        userSalt64 = (userDict[userName][0])
        userSalt = base64.b64decode(userSalt64)
        
        passTry = raw_input("\nEnter password: ")
        
        hashObj=hashlib.sha256()
        hashObj.update(passTry)
        hashObj.update(userSalt)
        hashDigest=hashObj.digest()
        passHash = base64.b64encode(hashDigest)
        userSalt64 = base64.b64encode(userSalt)
        
        
        if passHash == (userDict[userName][1]):
            del userDict[userName]
            print("\nUsername & password have been deleted\n")
        else:
             print("\nIncorrect password\n")
    else:
        print("\nUsername not in database")
    



def Exit():
    f = open('password.txt', 'w')
    for key,value in userDict.iteritems():
        f.write(key + ':' + value[0] + ':' + value[1] + "\n")
    f.close()
    quit()

if os.stat("password.txt").st_size==0:
    displayMenu();
else:
    read_in_file();
    displayMenu();





