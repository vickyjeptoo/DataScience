def palindrome():
    name=str(input('Your String'))
    reverse = name[::-1]
    print(name)
    print(reverse)
    if name==reverse:
        print('it is a palindrome')

    else:
        print('is not')

palindrome()

def leapyear():
    year=int(input('Input the year'))
    if year%4==0 or year%400==0 and year%100!=0:
        print('It is a leap year')
    else:
        print('It is not a leap year')

leapyear()