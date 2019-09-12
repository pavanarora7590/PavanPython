def pair_sum(a, b):   
    if len(a)<2:
        return
    seen = set()
    print type(seen)
    #output = set()
    count =0
    for x in a:
        target = b-x
        if target not in seen:
            seen.add(x)
        else:
            #output.add( ( (min(x,target)),max(x,target) ) )
            seen.remove(target)
            count+=1

    return count
suma=pair_sum ( [1,2,3,4,4,1,4,1,1,1,1,3,3,2,2,4,4,4],5)
print suma