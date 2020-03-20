Name = input("Enter a Name:")
n = len(Name)
for i in range(n):
    print('  '*(n-i-1),end='')
    for j in range(i+1):
        print(Name[j],end=' ')
    print("")    
