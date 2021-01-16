import sys
def main():
    NumofEntries = 0
    attrvaluelist = []
    data = open(sys.argv[1],'r')
    for x in data:
        if len(x) == 1: #skipping all empty lines in between as the sample file had
            continue
        else:
            y=x.split(' ') #split via space so all actual elements are stored
            valuelist = []
            if (y[0] == sys.argv[4]):
                NumofEntries = NumofEntries + 1 #track total entries of data
                for z in y:
                    if z != '': #ignoreing all whitespace or nullspace
                        valuelist.append(z)
                attrIndex = int(sys.argv[2])-1 #index provided as user input to select the attribute
                attrvaluelist.append(float(valuelist[attrIndex]))

    print('Number of valid entry for device',sys.argv[4],'is :', NumofEntries)
    print('sum of all values', round(sum(attrvaluelist),4))
    if NumofEntries > 0:
        print('min value is ', round(min(attrvaluelist),4), 'max value is ', round(max(attrvaluelist),4))
        #NOTE:-I had local pypi issue so could not get numpy, but I think mean() from numpy is better to use here and as its not available I had used simple average = sum/number of entries
        average = round((sum(attrvaluelist)/NumofEntries),4)
        print('The Average is ', average)

        NumofDistribution = int(sys.argv[3]) #User provided
        EachStep = (round(max(attrvaluelist),4) - (round(min(attrvaluelist),4))) /NumofDistribution
        bins=[]
        distributionbins = []
        for x in range(NumofDistribution+1):
            y=round((x*EachStep)+ min(attrvaluelist),8) #min and max are two ends and each step from min to max contributes to the bin
            bins.append(y)
            distributionbins.append(0)
        print(bins)
        for x in attrvaluelist:
            for i,y in enumerate(bins):
                if x < y or x==y:
                    distributionbins[i]+=1
        print('the distributionbins is as follow')
        for i,x in enumerate(bins):
            print(distributionbins[i],'  <  ',x)

main()