#Calculation 


#Modules 
import string

#Functions 

def calculation (experssion) :

    length = len(experssion)

    for value in experssion : 

        if (length <= 0) :
            print("Error in input")
            return(None)

        elif (length == 1) :

            if (type(check(value)) == int):
                print("The number", value, "is returned")
                return(value)

            else : 
                print("Error in input")
                return(None)

        elif (length == 2) :

            

        elif (length == 2) :


def check (value) :

    dictionary = { 0 : "0",
    1 : "1",
    2 : "2",
    3 : "3",
    4 : "4",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "9",
    "Addition" : "+",
    "Subtraction" : "-",
    "Multiplication" : "*",
    "Division" : "/" }

    if value in dictionary : 
        return(dictionary.get(value))

#def conversion (value) :



#__main__

experssion = input("Enter an expression : ")
