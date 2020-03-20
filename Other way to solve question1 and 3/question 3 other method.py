names = ['Kiran','kiran','rakesh', 'Ramesh', 'rakesH']
countnames = {}
for name in names:
    name = name.lower()
    if name in countnames:
        countnames[name] += 1
    else:
        countnames[name] = 1

print(countnames)
