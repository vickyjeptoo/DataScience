#functions
#BMI
def body_mass_index():
    weight=float(input('Enter your weight:'))
    height=float(input('Enter your height:'))
    answer=weight/height**2
    print("Your BMI is:",answer)

#body_mass_index()

#functions with parameters
#base&height are called parameters
#these parameters are unknown,we provide them during function call
def area(base,height):
    #base = 50
    #height =5
    answer=0.5*base*height
    print('Your area is:',answer)

area(base=50,height=5)


#function to calculate electricity bill
#Units is a parameter
def electricity(units):
    if units<=50:
        print('pay',units*3.40)

    elif units>=50 and units<=100:
        print('pay',units*4)

    elif units>=100 and units<=200:
        print('pay',units*4.50)
    else:
        print('pay',units*5.20)
#value=float(input('What are your units'))
electricity(units=444)
#parameters vs arguments
#parameters are defined in the function i.e def function(param1,param2,....)
#arguments are provided during function call to fit the defined parameters.
#write a function to convert kshs to any other currency(USD,EURO,YEN,RAND)

def convert_money(KES):
    print(KES*0.0096,'USD')
    print(KES*0.0087,'EURO')
    print(KES*1.05 ,'YEN')
    print(KES*0.14,'RAND')
value=float(input('Enter amount you wish to convert:'))
convert_money(KES=value)

#OOP-Object Oriented Programming
#create a function that check if a password has a Capital,Number,Symbol,not less than 8 letters.
#hint:ifs,re(regular expression)
#test :qweRT#123
