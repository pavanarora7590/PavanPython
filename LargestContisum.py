print 'find largest continuous sum from a list'
def largest_cont_sum (a):
    inc_sum = 0
    act_sum = 0
    final_sum = 0
    totallen = len(a)
    for x in range(totallen):
        inc_sum = inc_sum + a[x]
        if inc_sum > act_sum:
            act_sum = inc_sum
            final_sum = act_sum
        else:
            y = totallen-1
            if x < y:
                if inc_sum + a[x+1] > act_sum:
                    act_sum = inc_sum
                    final_sum = act_sum
                else:
                    act_sum = 0
                    inc_sum = 0
    return final_sum
a = [1,2,-1,3,4,10,10,-10,11]
x=largest_cont_sum(a)
print x