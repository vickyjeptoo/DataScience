#Ask the user to enter taxpayer's firstname, gross income, and number of children.

name=input("Enter taxpayer's first name")
gross_income=float(input("Enter gross income"))
children=int(input("Enter number of children"))

#Each taxpayer's tax due is computed as follows;
#The taxpayer's dependency exemption is determined by multiplying $3,000 times the number of children.

dependency_excemption = 3000*children

#The taxpayer's net income is determined by taking the taxpayer's gross income
# and subtracting the taxpayer's dependency exemption.

net_income = gross_income -dependency_excemption
print("net pay",net_income)

#If the taxpayer's net income is between 0 and 50,000, the tax due is 15% of net income,
if net_income <0:
    print("invalid input")
elif net_income>=0 and net_income<=50000:
    print("the tax due is",0.15*net_income)

#If the taxpayer's net income is over 50000, the tax due is 15% for the first 50000 and the remaining is taxed 25%.
elif net_income>50000:
    print("the tax due is" ,((0.15*50000)+(net_income-50000)*0.25))

else :
    print("try again!")