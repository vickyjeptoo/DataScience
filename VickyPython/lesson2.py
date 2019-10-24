# Learn what is a tuple/list
# make decisions
county = "Nairobi" #string
cash = 80000 #int
counties =("Nairobi","Mombasa" , "Nyeri","Nakuru","Narok") #tuple
budget = (500,300,9000,68000) #tuple of numbers
print(type(counties))
print(type(county))
print(type(cash))
print(type(budget))

print(counties)
print(budget)
print(counties[2])
print(counties[1:3]) #1-2
print(counties[1:]) #1 and above
print(counties[:4]) #3 and below

#lists
cars=['toyota','nissan','bmw','honda','mazda']
print(type(cars))
print(cars)
#when do you need a list and when do you need a tupple?
#tuples are immutable-static(can't add or remove)
#list are mutable - you can add or remove
#tuples use brackets,lists use square brackets
cars.append('jaguar')
cars.remove('toyota')
cars.insert(2,'mercedes')
print(cars)