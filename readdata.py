import sys

def main():
    listOfFeatures = readFeatures("./data/featurenames.txt")
    listofcars = readData("./data/DataSet.txt",listOfFeatures)


    # print(categorize(listOfFeatures, listofcars))


    # print("Features {0}".format(listOfFeatures)) 
    print("Example car {0}".format(listofcars[0]))

    """
    for el in listofcars:
        print(el['width'])
    """

    # struct = {
    #     min: sys.maxsize,
    #     max: sys.minsize,
    #     std: undef
    # }

    results = {}
    # Get Min Values
    for field in listOfFeatures:
        continuousResult = {
            "min": 0,
            "max": 0,
            "count":0,
            "cardinality": 0,
            "quart1": 0,
            "quart4": 0,
            "std":0
        }

        #For each continous value get the min
        if field in continuous:
            continuousResult['min'] = getMin(listofcars, field)  
            continuousResult['max'] = getMax(listofcars, field)  
            continuousResult['count'] = getCount(listofcars, field)  
            continuousResult['miss'] = getMiss(listofcars, field)


        results[field] = continuousResult
        print("{0}:\t\t\t{1}".format(field, continuousResult))



# Continuous is a list of strings that represent fields that contain continuous data
continuous = ["normalized-losses",
                "wheel-base",
                "ngth",
                "width",
                "height",
                "curb-weight",
                "engine-size",
                "bore",
                "stroke",
                "compression-ratio",
                "horsepower",
                "peak-rpm",
                "city-mpg",
                "highway-mpg",
                "price"]




# Read feature names from file
def readFeatures(filename):
    fields = []
    for line in open (filename):
        for word in line.strip().split(','):
            fields.append(word)
    return fields


#read in the data set
def readData(filename,listOfFeatures):
    listofcars = []
    for line in open(filename):
        car = {}
        templine = []
        for word in line.strip().split(','):
            templine.append(word) 
        i = 0

        for field in listOfFeatures:
            car[field] = templine[i]
            i = i + 1
        listofcars.append(car)
    return listofcars

#Check if a value is a float
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

#TODO : return min dont just print it
#Returns the min value from a data set
def getMin (inputdict,value):
    currentMin = sys.maxsize
    miss = 0
    for el in inputdict:
        if el[value] is '?':
            miss = miss + 1
        else:
            if currentMin > float(el[value]):
                currentMin = float(el[value])
    return currentMin

def getMax (inputdict,value):
    currentMax = 0
    miss = 0
    for el in inputdict:
        if el[value] is '?':
            miss = miss + 1
        else:
            if currentMax < float(el[value]):
                currentMax = float(el[value])
    return currentMax

def getMiss (inputdict,value):
    miss = 0
    for el in inputdict:
        if el[value] is '?':
            miss = miss + 1
    return miss

def getCount (inputdict,value):
    count = 0
    for el in inputdict:
        if el[value] is not '?':
            count = count + 1
    return count

main()



# print(minloses)

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
