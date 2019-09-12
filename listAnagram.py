'''
Created on sept 26, 2018
@author: pavan
'''
def isanagram(a,b):
    a=a.replace(' ','').lower()
    b=b.replace(' ','').lower()
    for x in a:
        for y in b:
            if x == y:
                a=a.replace(x,"",1)
                b=b.replace(x,"",1)
    if (a == b == ''):
        print 'it is anagram'
        return True
    else:
        print 'it is not anagram'
        return False 
a=raw_input('Enter string 1 here: ')
b=raw_input("enter string 2 here: ")
c=isanagram(a,b)
print c