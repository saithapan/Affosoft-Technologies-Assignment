names = ['Kiran','kiran','rakesh', 'Ramesh', 'rakesH']
countnames = {}
for name in names:
    name = name.lower() # => to make 'test' and 'Test' and 'TeST'...etc the same
    if name in countnames:
        countnames[name] += 1
    else:
        countnames[name] = 1

print(countnames)