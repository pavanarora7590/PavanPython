for i in range(5):
    print(i)
print('\n')
for i in range(11,15):
    print(i)
print('\n')
for i in range(21,30):
    if i == 21:
        continue
    if i > 23:
        break
    print(i)
print('\n')
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print (i,a[i])
print('\n')
def add(a,b):
    c=a+b
    print ('the addition is ',c)
add(45, 55)
