#loop through lists
counties = ['Kisumu','Meru','Nairobi','Narokk','Mombasa']
print(counties)
for county in counties:
    print(county)
    if county=='Narok':
        break
    else:
        continue
