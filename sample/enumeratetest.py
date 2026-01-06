seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))

print("Testing enumerate function:")
for index, season in enumerate(seasons):
    print(index, season)  


print("Testing enumerate with start index 1:")
for index, season in list(enumerate(seasons, start=1)):
    print(index, season)      