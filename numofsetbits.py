def fun1(n):
    coun = 0
    while n > 0:
        n = n & (n-1)
        coun += 1
    print ("number of set bits are %d" %(coun))
number = input("enter the number to get number of set bits in it: ")
fun1(number)
    
    

