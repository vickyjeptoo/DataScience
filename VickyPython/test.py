#create an account object
#states:name,balance,account number
#behaviour:deposit,withdraw
class Account:
     def __init__(self,name,balance,accno):
         self.name=name
         self.balance=balance
         self.accno=accno


     def deposit(self): #behaviour
         amount=float(input('how much are you depositing?'))
         print('your deposit amount is',amount,'KES')
         self.balance=amount+self.balance
         print('Your new balance is',self.balance,'KES')

     #     #client cannot withdraw more than the balance
     def withdraw(self):
         amount= float(input('how much are you withdrawing?'))
         if amount>self.balance:
             print('you have insufficient funds')
         else:

             print('you have withdrawn',amount,)
             print('availabale balance:',self.balance-amount)



 #instantiate class to make the object active.
 #object is an instance of Account...create an object#create an account object
#states:name,balance,account number
#behaviour:deposit,withdraw


object=Account(name='Vicky',balance=200 ,accno=1145788)
object.deposit()
object.withdraw()

#class patient
#tools we use in datascience that don't require python
#SPSS , Power Bi,tableue
#tableue online

