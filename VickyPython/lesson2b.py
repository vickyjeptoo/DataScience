#elif for multiple conditions

marks= float(input("What did you get?"))

if marks <0:
    print('negative')
elif marks<=50:
    print("you have failed")
elif marks >50 and marks <=75:
    print('Average')
elif marks >75 and marks <=90:
    print('above average')
elif marks >90 and marks <=100:
    print('excellent!')


else:
    print("wrong input!")#over 100