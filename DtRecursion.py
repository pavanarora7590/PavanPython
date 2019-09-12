'''recursion, calling fun within itself for e.g factorial, if N>1 n=n*fact(n)'''
from itertools import permutations
'''reverser a string via recursion--> logic is keep sending first char to last, so base case if len(str)==1 return str, else return rec(s[1:])+s[0]---> this will return rec[bcde]+a-->  rec[cde]+b + a'''
st1 = 'abcd'
def revstr (st1):
    if len(st1) == 1:
        return st1
    else:
        return revstr(st1[1:])+st1[0]
st2=revstr(st1)
print (st2)
perm = permutations([1, 2, 3], 2)
print (list(perm))
print (list(permutations(['ABCD'],2)))
def allperm (st1):
    if len(st1) == 1:
        return st1
    else:
        for i,let in enumerate(st1): #for every letter in string enumerate will be i-index and k-letter
            for perm in permutations( st1[:i] + st1[i+1:]): #for every permute of step2 and 3 for o to i index and i+1 to end, so all before me and after me letter
                out = out + [let + perm]
    return out

st2=allperm('abcd')
print (list(st2))