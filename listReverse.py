'''
Created on Feb 21, 2016

@author: pavan
'''
str1 = 'pavan'
str2 = str1[::-1]
list1=[]
print type(str1)
print str2
for i in str1:
    list1.insert(0,i)
print list1
    