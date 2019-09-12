import subprocess
import time
numofloop = int (input ('Enter the number of readings you want to take,NOTE:-limit your input between 1-5 and numeric only; else default of 5 value if you enter anything other then 1-5: '))
print '\nASSUMPTION1:- libraries needed to run netperf command will be there in system'
print 'ASSUMPTION2:- output will always be in bits/sec and always numeric in base10'
print 'ASSUMPTION3:- This script wont work if the output is in hex for x^ybits/sec so if x or y is in nondecimal this script is limited'
def getavgreadings(numofloop):
    y = int(numofloop)
    if ( y < 1 or y > 5):
        print 'The number of readings the user wants is not in the range 1-5 or not a integer so your input is ignored and the results will be calculated with 5 readings'
        checkloopreading = 5
    else :
        checkloopreading = y
    for i in range(0,checkloopreading):
        instr = subprocess.check_output(['netperf'])
        print instr
        powerval = int(instr[instr.index('^')+1:instr.index('bits/sec')])
        baseval = int(instr[instr.index('secs.')+6:instr.index('^')])
        dataset.append(int(baseval)**int(powerval))
        i += 1
        time.sleep(1)
    total = 0
    for x in dataset:
        total += x
        average = total/checkloopreading
    return int(average)
dataset = []
av = getavgreadings(numofloop)
print '\nThe average is ', av
print '\n\nSAVE this result into a FILE preferably into CSV formart with NUMBER into one field and UNIT-bits/sec in another field, also save TIMESTAMP so all comparision becomes easy'
print '\nIf it will be a unix system, a cron job schedule will also help to just run the script every day or at every defined itnernval and save results'
print '\nDepending on the need, a email mechanism can also be trigeered for daily results, or for results which are critical like 0 throughout to propogate system is having issues via a email marked with high importance etc'