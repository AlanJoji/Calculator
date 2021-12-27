#Calculation 


#Modules 
import string

#Functions 

def summation (expression_list, length, position) :

    if (position == 0) :
        return(0)

    elif (position == length - 1) : 
        return(False)
    
    else :
        return(expression_list[position - 1] + expression_list[position + 1])

def subtraction (expression_list, length, position) :

    if (position == 0) :
        return(0)

    elif (position == length - 1) : 
        return(False)
    
    else :
        return(expression_list[position - 1] - expression_list[position + 1])

def multiplication (expression_list, length, position) :

    if (position == 0 or position == length - 1) :
        return(False)
    
    else :
        return(expression_list[position - 1] * expression_list[position])

def division (expression_list, length, position) :

    if (position == 0 or position == length - 1) :
        return(False)
    
    else :
        return(expression_list[position - 1] / expression_list[position])
              
def check (value) :

    dictionary = { "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "+" : "+",
    "-" : "-",
    "*" : "*" ,
    "/" : "/" }

    if value in dictionary :
        #print("Value", value, ", Result", dictionary.get(value)) 
        return(dictionary.get(value))
    
    else : 
        return(False)

def calculation (expression) :

    length = len(expression)

    if (length <= 0) :
            print("Error in input")
            return(False)

    elif (length == 1) :

        for value in expression : 

            if (type(check(value)) == int):
                print("The number", value, "is returned")
                return(value)

            else : 
                print("Error in input")
                return(False)

    elif (length == 2) :

        if (type(check(expression[0])) == str) :
            
            if (type(check(expression[1])) == int) :
                print("The result of the expression :",expression)
                return(expression)
            
            else :
                print("Error in input")
                return(False)
        
        elif (type(check(expression[0])) == int) :

            if (type(check(expression[1])) == int) :
                print("The result of the expression :",expression)
                return(expression)
            
            else :
                print("Error in input")
                return(False)
            
    else : 

        if (expression.isdigit() == True) :
            print("The result of the expression :", expression)
            return(expression)

        else :

            initial_expression_list = []

            for value in expression :

                result = check(value)
                initial_expression_list.append(result)

            print(initial_expression_list)
            expression_list = []

            #Final Location

            for x in initial_expression_list :

                if (type(x) == str) :
                    expression_list.append(x)
                    initial_expression_list #Here
                
                else :





            length = len(expression_list)

            for position in range (0, length) :

                if (type(expression_list[position]) == str) :

                    if (expression_list[position] == "+") :
                        storage = summation(expression_list, length, position)
                    
                    if (expression_list[position] == "-") :
                        storage = subtraction()
    
                    

#__main__

expression = input("Enter an expression : ")
calculation(expression)

#Comment for test commit 