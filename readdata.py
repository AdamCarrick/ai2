import sys
from statistics import *

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

def main():
    listOfFeatures = readFeatures("./data/featurenames.txt")
    listofcars = readData("./data/DataSet.txt",listOfFeatures)

    continuousresults = {}

    for field in continuous:
        fieldValues = getFieldsAsFloat(listofcars, field)
        if len(fieldValues) > 0:
            continuousresults[field] = {
                "min": min(fieldValues),
                "max": max(fieldValues),
                "count": len(fieldValues),
                "cardinality": variance(fieldValues),
                "quart1": median_low(fieldValues),
                "quart4": median_high(fieldValues),
                "std": stdev(fieldValues)
            };


    carCounts ={}
    fields = []

    notcontinuous = set(listOfFeatures) - set(continuous)
    for field in notcontinuous:
        fieldValues = getFieldsAsString(listofcars, field)
        if len(fieldValues) > 0:
            carCounts[field] = {
                # "raw": fieldValues,
                "counts": getWordCounts(fieldValues) 
            };
            fields.append(field)
    
    # print(carCounts)
    mode = getMode(carCounts, fields)        
    for key in mode:
        print("{0} mode: {1} ({2}) mode2: {3} ({4})".format(key['field'], key['mode'], key['count'],key['mode2'], key['count2']))
        

def getWordCounts(collection):
    # print(collection)
    results = {}
    for word in collection:
        try:
            results[word] = results[word] + 1
        except:
            results[word] = 1
    return results

def getFieldsAsFloat(collection, field):
    results = []
    for car in collection:  
        try:
            results.append(float(car[field]))
        except:
            pass

    return results

def getFieldsAsString(collection, field):
    results = []
    for car in collection:
        value = car[field]  
        if value is not '?':
            results.append(value)

    return results







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

def getMode(carCounts,fields):
    # print(fields) #['num-of-doors', 'aspiration', 'engine-location', 'length', 'fuel-type', 'symboling', 'num-of-cylinders', 'fuel-system', 'body-style', 'drive-wheels', 'engine-type', 'make']
    # print(carCounts) 
    
    results = []

    for field in fields:
        collection = carCounts[field]
        # print("{0}: {1}".format(field, collection['counts']))
        counts = collection['counts']
        # print(counts.keys())
        # print(counts.keys)
        keys = counts.keys()
        currentMax = 0
        previousMax = 0
        modeValue = ''
        modeValue2 = ''
        for key in keys:
            # print ("{0}: {1}".format(key, counts[key]))
            value = int(counts[key])
            if value > currentMax:
                    previousMax = currentMax
                    modeValue2 = modeValue
                    currentMax = value
                    modeValue = key
                    

                    # TODO: Save the previous one as well

        # print("{0} mode: {1} ({2})".format(field, modeValue, currentMax))
        singleResult = {
                "field" : field,
                "mode" : modeValue,
                "count" : currentMax,
                "mode2" : modeValue2,
                "count2" : previousMax
        }

        print(singleResult)
        results.append(singleResult)
    return results

# def getCardinality(inputdict, field):
#     cardinality =0
#         inputlist =[]
#     for el in inputdict:
#         if el[field] is not '?':
#             inputlist.append(float(el[field]))
#     std = statistics.stdev(inputlist)
#     return std 
#     return cardinality

main()
