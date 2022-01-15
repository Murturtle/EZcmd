import time
import random
import os
import threading
from icmplib import ping

os.system("@echo off")
os.system("title EZcmd")
color = "white"
print('Welcome to EZcmd\nFor help type "help"\n')

def cmd():
    main = input('<|> ')
    if main == "":
        cmd()

    elif main == "help":
        print("+=+=+=+=+=+=+=+=+=+=  Commands  +=+=+=+=+=+=+=+=+=+=")
        print("help - shows This Message")
        print("about - shows information about EZcmd")
        print("exit - quits EZcmd")
        print("")
        print("shutdown - turns off your computer")
        print("")
        print("clear - clears the screen")
        print("color - changes the color of text")
        print("theme - changes the theme")
        print("")
        print("calc - basic calculator")
        print("")
        print("3d - 3D cube")
        print("noise - generates noise")
        print("")
        print("superping - floods the host with pings")

    elif main == "exit":
        print("exiting EZcmd")
        time.sleep(1)
        os._exit()
    
    elif main == "about":
        print("v2.0")
        print("By Murturtle \n")
    
    elif main == "shutdown":
        print("shutting down\n")
        time.sleep(1)
        os.system("shutdown /s /t 1")
      
    elif main == "clear":
        os.system("cls")
        cmd()

    elif main == "color":
        print("Valid Colors: white, green, red, purple, aqua, or blue \n")
        color = input("<Color> ")

        if color == "white":
            os.system("color 7")
        
        elif color == "red":
            os.system("color 4")
        
        elif color == "purple":
            os.system("color 5")
        
        elif color == "green":
            os.system("color 2")
        
        elif color == "aqua":
            os.system("color 3")
        
        elif color == "blue":
            os.system("color 1")

    elif main == "theme":
        print("Valid Themes: dark, light, yellow, and hacker  \n")
        theme = input("<Theme> ")

        if theme == "dark":
            os.system("color 0f")
        
        elif theme == "light":
            os.system("color f0")
        
        elif theme == "yellow":
            os.system("color 6f")
        
        elif theme == "hacker":
            os.system("color 02")
        
        elif theme == "evil-hacker":
            os.system("color 04")
        cmd()
    
    elif main == "calc":
        print('Basic: add, sub, mul, and div | Complex: abs | Type "exit" to exit  \n')
        def calculator():
            calc = input("<Calc> ")

            if calc == "exit":
                cmd()

            elif calc == "add":
                num1 = float(input("<Calc | Num1> "))
                num2 = float(input("<Calc | Num2> "))
                print(num1+num2)
            
            elif calc == "sub":
                num1 = float(input("<Calc | Num1> "))
                num2 = float(input("<Calc | Num2> "))
                print(num1-num2)
            
            elif calc == "mul":
                num1 = float(input("<Calc | Num1> "))
                num2 = float(input("<Calc | Num2> "))
                print(num1*num2)
            
            elif calc == "div":
                num1 = float(input("<Calc | Num1> "))
                num2 = float(input("<Calc | Num2> "))
                print(num1/num2)
            
            elif calc == "abs":
                num1 = float(input("<Calc | Num1> "))
                print(abs(num1))
            
            else:
                print("operation not found \n")
            calculator()
        calculator()
    
    elif main == "3d":
            print("   _______________")
            print("  /              /|")
            print(" /              / |")
            print("/______________/  |")
            print("|             |   /")
            print("|             |  /")
            print("|             | /")
            print("|             |/")
            print("|_____________/")
            print("")
    
    elif main == "noise":

        for i in range(4):
            rand = random.randint(1,2)
            rand = 5 - rand
            rand1 = random.randint(2,3)
            rand1 = 5 - rand1
            rand2 = random.randint(3,4)
            rand2 = 5 - rand2
            rand3 = random.randint(4,5)
            rand3 = 5 - rand3
            print(str(rand)+" "+str(rand1)+" "+str(rand2)+" "+str(rand3))
    
    elif main == "superping":
        host = input("<IP> ")
        print("[WARN] This will us up alot of you cpu")
        print("[INFO] Press (X) to exit")
        time.sleep(3)
        def pinger():
            while(True):
                ping(host,1,interval=0,timeout=0,source=None,privileged=False)
                print("[INFO] Ping sent")
        for i in range(99999):
            pingthread = threading.Thread(target=pinger)
            pingthread.start()


    else:
        print('error command "' + main +'" not found')
    cmd()

cmd()
