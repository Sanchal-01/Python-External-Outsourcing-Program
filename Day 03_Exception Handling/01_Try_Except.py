# Check vs  Uncheck Exception :
# Before Runtime vs at Run Time Exception

name = input("Enter your favourite exercise: ")
def exercise(name):
        if (name == "running"):
                print("Running is a good exercise")
        else:
                print("This is not good")

exercise(name)

#------------------------------------------------#----------------------------------------------------------#--------


a = 10
b = 0

try:
    print(a/b)
except:
    print("Division by zero not allowed")


#------------------------------------------------#----------------------------------------------------------#--------

# TASk 1:
    a = int( input("Enter a number"))
    try:
        print(100/a,"Division is done!!")

    except ZeroDivisionError as e:
        print("Zero se divide nahi kar sakte.",{e})
    except ValueError:
        print("Sirf Numbers enter karo.")
    except Exception as ex:
        print("Division not allowed.", {ex})
       
#------------------------------------------------#----------------------------------------------------------#--------


# FINALLY BLOCK 


a = 10
b = 5

try:
    print(a/b)
except:
    print("Division by zero not allowed")

finally:
     print("Finally block also executed")    # Even if there not an error in the code finally block will always be executed.

#---------------------------------------------#-------------------------------------------------#------------------------

def exception():
    try:
        num1 =int(input("enter the number 1:"))
        num2 =int(input("enter the number 2:"))
        return(num1/num2)


    except ZeroDivisionError:
        print("Division by Zero  nahi karna chahiye tha.")

    except ValueError as e:
        print("Please enter integer only", {"This is not cool"})

exception()