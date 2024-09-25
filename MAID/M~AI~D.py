# CORTANA
import random
import time
import datetime

def Register():
    global USER
    dB = open('dataBase.txt', 'r')
    USER = input("What should i call You: ")
    passw = input("Create a Pasword: ")
    passw1 = input("Confirm Password: ")
    u = []
    p = []

    for i in dB:
        a,b = i.split(", ")
        b = b.strip()
        u.append(a)
        p.append(b)
    data = dict(zip(u, p))
    print(data)

    if passw != passw1:
        print("passwords don't match, restart")
        Register()

    else: 
        if len(passw) < 8:
            print(USER + ' password should\'nt be less than 8 characters' '\n' 'try again')
            Register()



        elif USER in u:
            print("Username exists")
            Register()
        
        else:
            dB = open('dataBase.txt', 'a')     
            dB.write(USER + ', ' + passw + '\n')
            Maid()





def Maid():
    print('Welcome! ', end = '')
    global f

    print('Should I create you a Diary')
    cD = input('yes/no: ')
    
    if cD != 'yes':
        print('Please answer with either a yes or no')

    if cD != 'no':
        print('Please answer with either a yes or no')
    
    if cD == 'yes':
        print('ok creating DIARY ' '.', end = '')
        time.sleep(2)

        print('.', end = '')
        time.sleep(2)

        print('.')
        time.sleep(2)

        print('please choose file format(pdf or txt) :')
        fileFormat = input()

        if fileFormat == 'pdf':
            f = open(USER + "'s Diary.pdf", "x")

        if fileFormat == 'txt':
            f = open(USER + "'s Diary.txt", "x")
        time.sleep(3)

x = datetime.datetime.now()

def chatFile(): 
    global Gooday
    chat = input()
    Gooday = ["How are you " + USER, "Hope you're Good " + USER, "Goodday " + USER]   
    hi = random.choice(Gooday)
    print(hi)

    y = x.year
    y = str(y)
    f.write(y)
    f.write('MAID: ' + hi)
    f.write(USER + ': ' + chat)



Register()



