#functions,dictionary..
#functions - block of code that performs a specific task

def add ():
    x=78
    y=56
    answer= x+y
    print('Your solution is',answer)


def simple_interest():                          #defining a function
    principle=float(input("input principle"))
    rate = float(input("input rate"))
    time = int(input("input time"))
    answer=principle*rate*time
    print('Your interest is',answer)


#prac:create a function to check the largest number from 3 variables


def largest_number():
    x=float(input("enter your first number:"))
    y=float(input("enter the second number:"))
    z=float(input("enter the third number"))
    if x>y and x>z:
        print(x,"Is the largest number!")

    elif y>x and y>z:
        print(y,"Is the largest number!")

    else:
        print(z,"Is the largest number!")

#simple_interest()#call function
#add()
#largest_number()
#Adv of functions
#well organized code & easy to read
#functions are re-usable
#create a function and find average of 3 numbers

def average():
    x=float(input("enter num1"))
    y=float(input("enter num2"))
    z=float(input("enter num3"))

    print('average is',x+y+z/3)

average()