print 'lists are immutable mix of int and strings, can refer to elements via index, can append in end and can remove elements without index'
d = [1,2,3]
print type(d)
d.append('hello')
print d
d.remove(2)
print d
print '\ncan overwrite elemnent at specific index via setting any index, for reverse set it as negative '
d[0] = 5
d[-1] ='ello'

print '\nlearning loops so a basic example'
a = [1,2,3,4]
for x in a:
    print x,a

print '\nloops from a x to y index, so here are printing index 0 1 2 elements which are 9 8 and 7'
a = [9,8,7,6,5,4,3,2]
print a
for x in range(0,3):
    print x,a[x]

print '\ninsert(adding extra) at specific index for e.g revere a list, just keep adding at 0 index'
c = []
for x in d:
    c.insert(0,x)
print d
print c

print '\none liner for revere a list/string'
x = c[::-1]
print x
print c

print '\ninbuilt compare function to compare both, but if int and string are compared it different'
x=cmp(c,d)
y=cmp(d,c)
print c, d, x
print d,c, y
print '\nif all integers it just check elements one by one and returns response, 1 if first is greater, -1 is smaller and 0 if same'
h=[1,2,3,4]
g=[-5,1,1,1]
x=cmp(h,g)
y=cmp(g,h)
print h, g, x
print g, h, y
print 'see the diff'
h=[1,2,3,4]
g=[1,2,5,4]
x=cmp(h,g)
y=cmp(g,h)
print h, g, x
print g, h, y
print '\nlist(a) and if a is tuple now its type conversion'
print 'other list FUNCTIONS are len(list) max(list) min(list)'
print 'other list methods are x=index, 5=value for all expamples'
print 'List.appends(5) list.count(5) list.extend(list2)'
list1 = [1,2,4,5,5]
list1.append(5)
print 'count is %d' %list1.count(5)
list2=[33,44]
list1.extend(list2)
print list1 
print '\nlist.index(x) list.insert(x,5, list.pop(x), list.remove(5)'
print 'index of 33 is %d' %list1.index(33)
list1.insert(6,333)
print '\ninserted new element 333 at index 6 now'
print 'index of 33 is %d' %list1.index(33)
print 'index of 333 is %d' %list1.index(333)
print '\npop element at index 8 which is 44 now'
list1.pop(8)
print list1
print '\nlist.reverse() list.sort(list1)'
list1.reverse()
print 'reverse of list is %s' %list1
list1.sort()
print '\ndefault sorting is ascending %s' %list1
list1.sort(reverse=True)
print '\nREVERSE TRUE as argument in sort will  sorting sorting is decending %s' %list1
list1=['a', 'aa', 'bbb', 'd', 'aaaaaaa', 'cc']
list1.sort(key=len)
print '\nKEY FUNCTION will run the function on element and then sort the result of func'
print 'in this example we are comparing length of each element'
print list1
print '\nwe can also have our own function which will say return just last element of string and then strings will be compared based on that'
print 'we can also have key = str.lower which will convert all to lower first and then compare'
print 'PLAY with your own/inbuilt functions to manipulate sorting as per your needs'
