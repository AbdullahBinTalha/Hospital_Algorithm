# A program for Hospital Algorithm

import random as R
import time as T
##################### FUNCTIONS AREA #######################################

def DOC():
    T.sleep(0)
    print(".")
    T.sleep(1)
    print(".")
    T.sleep(2)
    List1 = ["Dr.Shakeel", "Dr.Osama","Dr.Muneeb","Dr.Karim"]
    print(R.choice(List1))
    
def NUM():
    T.sleep(1)
    print("MAKE")
    print("SURE")
    T.sleep(1)
    print("NOT")
    print("TO")
    T.sleep(1)
    print("MISPLACE")
    print("IT")
    Tuple1 = ("1","2","3","4","5","6","7","8","9","10")
    T.sleep(3)
    print("-------------------------------------")
    print(R.choice(Tuple1))

def Info():  
    global Name
    global Age
    global Gender
    Name = input("Enter your name: ")
    print("-------------------------------------------")
    Age = int(input("Enter your age: "))
    print("-------------------------------------------")
    Gender = input("Enter your Gender: ")

def VM():
    global dict1

    dict1 = {
        1:"Chips",
        2:"Coke",
        3:"Red Bull",
        4:"Water Bottle",
        5:"Iced Tea"
    }
    return dict1

###########################################################



# start of code
print("-------------------------------------------")
print("WELCOME TO THE CURRUPTED HOSPITAL")
print("-------------------------------------------")
print("What type of Case do you have")
Patient = input("a:Emergency, b:Not Urgent: ")
print("----------------------------------------------")

# giving the conditions

if Patient == "a":
    print("Ok!,so you have an Urgency")
    print("Please give us the requirements;")
    print("----------------------------------------")
    Info()
    print("Here is your Bio")
    print("---------------------------------------")
    # making a class for patient's bio
    class Patient_Bio:
        Your_name = Name
        Your_Age = Age
        Your_Gender = Gender
        def Bio(self):
            print (f"Your name is",{Name})
            print (f"Your Age is",{Age})
            print (f"Your Gender is",{Gender})
    p1 = Patient_Bio()
    # print(Patient_Bio.Your_name)  we could have used this but it is not a good practise
    # print(Patient_Bio.Your_name)
    # print(Patient_Bio.Your_Gender)
    p1.Bio()
    print("---------------------------------------------")
    T.sleep(1)
    print("Here is your card number")
    NUM()
    print("---------------------------------------------")
    print("-----Ok so according to your case the Doctor we should asign you will be-----")
    DOC()
    print("now please go to the emergency ward")
    print("and you will meet up with the Doc")

############################################################################################
elif Patient == "b":
    print("ok so you can wait!")
    T.sleep(1)
    print("please fill the form")
    print("-------------------------------------------------")
    Info()
    print("Here is your Bio")
    print("---------------------------------------")

    class Patient_Bio:
        Your_name = Name
        Your_Age = Age
        Your_Gender = Gender
        def Bio(self):
            print (f"Your name is",{Name})
            print (f"Your Age is",{Age})
            print (f"Your Gender is",{Gender})
    p1 = Patient_Bio()
    # print(Patient_Bio.Your_name)  we could have used this but it is not a good practise
    # print(Patient_Bio.Your_name)
    # print(Patient_Bio.Your_Gender)
    p1.Bio()
    print("---------------------------------------------")
    T.sleep(1)
    print("Here is your card number")
    NUM()
    print("---------------------------------------------")
    print("-----Ok so according to your case the Doctor we should asign you will be-----")
    DOC()
    print("Now please take a seat and wait for your number to show")
    print("---------------------------------------------------------")
    T.sleep(1)
# asking for vending machine
    print("While you wait would you like to get some thing from our vending machine")
    vending_machine = input("y/n: " )

    if vending_machine == "y":
        print("-----------WELCOME TO THE VENDING MACHINE----------------------")
        T.sleep(1)
        print(VM())
        processing = int(input("what do you need, write the item's number: "))

        if processing in dict1:
            Tuple2 = ("1","2","3","4","5","6","7","8","9","10")
            form = R.choice(Tuple2)
            txt = ("ok so it will be {}.00$")
            print(txt.format(form))
    else:
        print("ok so happy wait.......")

else:
    print("There is no available service like this")