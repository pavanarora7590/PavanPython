'''
Created on Feb 21, 2016

@author: pavan
'''
import os
print os.name
print os.getcwd()
os.chdir('C:\Users\pavan\Desktop')
print os.getcwd()
'''open and find directory and then change directory'''
print tuple(os.listdir(os.getcwd()))
#print dir(os)
p = os.path.join(os.getcwd(),'\\abc')
print p
q = os.path.join(os.getcwd(),'abc')
print q
r = os.path.join(os.getcwd(),'\abc')
print r


'''open a file and read lines'''
f = open('C:\Users\pavan\Desktop\sticky.txt', 'r')
#ab = list(f.readlines())
#print len(ab)
''' list of strings'''
#print f.readlines() 
'''single string whole file'''
#print f.read()
'''one by one each line and '' for end of file''' 
print f.readline()
f.seek(149)
print f.readline()

for line in f.readlines():
    print line



    