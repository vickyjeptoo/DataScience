#elif statement

age=float(input('what is your age?'))
ticket_price=float(input('input ticket price'))
if age <0:
    print("invalid input!")
elif age>=65:
    print('$',ticket_price*0.5,'Given 50 % discount')
elif age<6:
    print('$',0 , 'Given 100 % discount')
else :
    print('$',ticket_price,"No discount given!")

#https://justpaste.it/4748k