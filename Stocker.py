import smtplib   //pip install '--------' => to install packages
import random
from time import sleep
import os
# from email.message import EmailMessage
import FileHandling
from tkinter import *
from tkinter import messagebox


# def finalProcess():
#     sleep(1)
#     print('\n\n\t\t       Completeting Process.......')
#     sleep(1)
#     print('\n\t\t      Please Wait ...............')
#     sleep(4)
#     print('\n\t\t      Almost there ..............')
#     sleep(3)

def messageBox():
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()

    if not messagebox.askyesno('Warning', 'Do You Want To Exit ?'):
        main()
    else:
        exit()

    window.deiconify()
    window.destroy()
    window.quit()


def intro():
    os.system('cls')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t       WELCOME TO')
    sleep(2)
    os.system('cls')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t   THE STOCKER - THE ONLY STOCK KEEPING APP')
    sleep(5)
    os.system('cls')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\tGetting Everthing Ready')
    sleep(9)
    os.system('cls')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\tAlmost there')
    sleep(6)
    os.system('cls')
    main()

def private():
    os.system('cls')

    x = int(input("\tEnter The Password: "))
    if x == 2856:
        os.system('cls')
        print("\t\t  =================================================================================")
        print("\t\t                                       PRIVATE ZONE                        ")
        print("\t\t  =================================================================================")
        print("\t\t             1. Add Items ")
        print("\t\t             2. Edit Items")
        print("\t\t             3. Delete Items")
        print("\t\t             4. Search Item With Details")
        print("\t\t             5. Show All Item With Details")
        print("\t\t             6. Go Back To The Main Page ")
        print("\t\t             7. Exit The App")
        print('\t\t  =================================================================================\n')
        option = int(input('\n\t\t             Enter Your Choice:-(Enter The Id Of The Option): '))
        if option == 1:
            os.system('cls')
            print(" ====================================================")
            print("                       ADD ITEMS                      ")
            print(" ====================================================")
            id = str(input('\n  Enter The Item\'s ID: '))
            name = str(input('  Enter The Item\'s Name: '))
            price = str(input('  Enter The Item\'s Price: '))
            mode = str(input('  Enter The Item\'s Mode: '))
            FileHandling.AddEditDeleteSearch.addData(id, name, price, mode)
            print("\n\n  Item added successfully.........")
            input('Press \'Enter\' To Go Back To Private Zone.......')
            private()

        elif option == 2:
            os.system('cls')
            print(" ====================================================")
            print("                       EDIT ITEMS                      ")
            print(" ====================================================")
            mid = str(input('\n  Enter The Item\'s ID To Be Edited: '))
            FileHandling.AddEditDeleteSearch.edit(mid)
            print("\n\n  Item edited successfully.........")
            input('Press \'Enter\' To Go Back To Private Zone.......')
            private()

        elif option == 3:
            os.system('cls')
            print(" ====================================================")
            print("                       DELETE ITEMS                      ")
            print(" ====================================================")
            did = str(input('\n  Enter The Item\'s ID To Be Deleted: '))
            FileHandling.AddEditDeleteSearch.delete(did)
            print("\n\n  Item deleted successfully.........")
            input('Press \'Enter\' To Go Back To Private Zone.......')
            private()

        # Search Item With Details
        elif option == 4:
            os.system('cls')
            print(" ====================================================")
            print("                       SEARCH ITEMS                  ")
            print(" ====================================================")
            uid = str(input('\n  Enter The Item\'s ID: '))
            FileHandling.search(uid)
            input('\nPress \'Enter\' To Go Back To Main Page ..........')
            private()

        # Show All Item With Details
        elif option == 5:
            os.system('cls')
            print(" ====================================================")
            print("                       TOTAL ITEMS                  ")
            print(" ====================================================")
            FileHandling.AddEditDeleteSearch.getData()
            input('\nPress \'Enter\' To Go Back To Main Page ..........')
            private()

        elif option == 6:
            main()

        elif option == 7:
            # messageBox()
            exit(0)
    else:
        private()



def main():
    os.system('cls')
    print("\t\t  =================================================================================")
    print("\t\t                       STOCKER - THE ONLY STOCK KEEPING APP                        ")
    print("\t\t  =================================================================================")

    print("\t\t             1. Edit / Delete / Add items (Password Protected) ")
    print("\t\t             2. Billing Counter")
    print("\t\t             3. See Item Details")
    print("\t\t             4. Search Item With Details")
    print("\t\t             5. Exit The App")
    print('\t\t  =================================================================================')
    option = int(input('\n\t\t             Enter Your Choice:-(Enter The Id Of The Option): '))
    if option == 1:
        private()

    elif option == 2:
        pass

    elif option == 3:
        os.system('cls')
        print(" ====================================================")
        print("                       TOTAL ITEMS                  ")
        print(" ====================================================")
        FileHandling.AddEditDeleteSearch.getData()
        input('\nPress \'Enter\' To Go Back To Main Page ..........')
        main()

    elif option == 4:
        os.system('cls')
        print(" ====================================================")
        print("                       SEARCH ITEMS                  ")
        print(" ====================================================")
        uid = str(input('\n  Enter The Item\'s ID: '))
        FileHandling.search(uid)
        input('\nPress \'Enter\' To Go Back To Main Page ..........')
        main()

    elif option == 5:
        # messageBox()
        exit(0)

def progressBar():
    i = 1
    while i <= 10:
        sleep(1)
        print('||', end='')
        i = i + 1


# def addStorage(add: str):
#     with open('gmail.txt', 'a') as f:
#         f.write(add)


def Gmail(userId):
    id = 'jayden.hauff21@gmail.com'
    pawd = 'koi357Uk'
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        otp = int(random.randint(100000, 999999))
        smtp.login(id, pawd)
        subject = 'Verification of the E-mail Address'
        body = f'Your OTP for verification is {otp}. Please enter this OTP in the application to complete the login process'
        msg = f'Subject: {subject}\n\n\n{body}'
        smtp.sendmail(id, userId, msg)
        print('\n\t\t       Email Sent To The Entered Email Address')
    return otp


def login():
    os.system("cls")
    print("\t\t  ====================================================")
    print("\t\t                        LOGIN                        ")
    print("\t\t  ====================================================")
    print("\n\t\t        Please Login Using Your Gmail Account----")

    uId = input("\n\n\t\t       Enter Your Gmail ID: ")
    otp = Gmail(uId)

    uotp = int(input('\n\t\t       Enter The OTP: '))

    if uotp == otp:
        intro()

    else:
        print('\t\t      Sorry! The OTP is wrong.....\n\t\t      Please try again......')
        sleep(2)
        login()


login()
