import sys


listofcars = []
listOfFeatures = []

for line in open ("./data/featurenames.txt"):
    for word in line.strip().split(','):
        listOfFeatures.append(word)


for line in open("./data/DataSet.txt"):
    car = {}
    templine = []
    for word in line.strip().split(','):
        templine.append(word) 
    i = 0
    for el in listOfFeatures:
        car[el] = templine[i]
        i = i + 1
    listofcars.append(car)





#print(listOfFeatures) 
#print(listofcars[0])

"""
for el in listofcars:
    print(el['width'])
"""

def getMin (inputdict,value):
    minloses = sys.maxsize
    miss = 0
    for el in inputdict:
        if el[value] is '?':
            miss = miss + 1
        else:
            if minloses > float(el[value]):
                minloses = float(el[value])



mindict = {}

# Get Min Values
for el in listOfFeatures:
    #For each continous value get the min
    mindict[el] = getMin(listofcars, el) 



print(minloses)

"""
descriptions = []
continuous = []
for litem in listofcars:
    dindex = [1,3,4,5,6,7,8,9,15,16,18]
    card = []
    carc = []
    for li in dindex:
        card.append(litem[li-1])
    descriptions.append(card)
    cindex = [2,10,11,12,13,14,17,19,20,21,22,23,24,25,26]
    for li in cindex:
        carc.append(litem[li-1])
    continuous.append(carc)

print(descriptions[0])
print(continuous[0])

table = {}
minloses = sys.maxsize
miss = 0
"""
"""
i = 0;
count = 0;
for li in continous:
    
    
    # get Cardinality
    # get min
    # get 1st quart
    # get mean
    # get median
    # get 3rd Quart
    # get max
    # get Std Deviation 
    if li[1] = '?':
        # get miss
        miss = miss+1
    if li[1] != '?':
        # get Count
        count = count +1
        if minloses > int(li[1]):
            minloses = int(li[1])
"""

"""

# Get the min value for each feature stored in the continuous table

for li in continuous:
    for el in li:
        table[ el : 'min'] = 
        print (el)
        



print (" Min losses = " + str(minloses))
"""
