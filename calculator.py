import colorama
from colorama import Fore, Back, Style
def add(a,b):
    print(Style.BRIGHT+Fore.RED+"RESULT",a+b)
def multiple(a,b):
    print(Style.BRIGHT+Fore.RED+"RESULT",a*b)
def divide(a,b):
    print(Style.BRIGHT+Fore.RED+"RESULT",a/b)
def reminder(a,b):
    print(Style.BRIGHT+Fore.RED+"RESULT",a%b)
def subtract(a,b):
    print(Style.BRIGHT+Fore.RED+"RESULT",a-b)
colorama.init(autoreset=True)
while True:
    print(Style.BRIGHT+Fore.MAGENTA+"*****************")
    print(Style.BRIGHT+Fore.GREEN+"1#ADDITION")
    print(Style.BRIGHT+Fore.GREEN+"2#MULTIPLICATION")
    print(Style.BRIGHT+Fore.GREEN+"3#DIVISION")
    print(Style.BRIGHT+Fore.GREEN+"4#REMINDER")
    print(Style.BRIGHT+Fore.GREEN+"5#SUBTRACTION")
    print(Style.BRIGHT+Fore.RED+"6#Exit")
    print(Style.BRIGHT+Fore.MAGENTA+"*****************")
    user_choice=str(input(Style.BRIGHT+Fore.CYAN+"Enter Funtion Number Which You want to Use:"))
    try:
        if(user_choice=="6"):
            print(Style.BRIGHT+Fore.RED+"Program Terminated")
            break
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        if(user_choice=="1"):
            add(a,b)
        elif(user_choice=="2"):
            multiple(a,b)
        elif(user_choice=="3"):
            divide(a,b)
        elif(user_choice=="4"):
            reminder(a,b)
        elif(user_choice=="5"):
            subtract(a,b)
        else:
            print(Style.BRIGHT+Fore.RED+"Your Input is Not Valid",user_choice)
    except Exception as any_error:
        print(Style.BRIGHT+Fore.RED+"Error",any_error)
    
print()

