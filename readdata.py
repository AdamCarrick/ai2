import sys
from statistics import *

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


    categoricalresults ={}

    notcontinuous = set(listOfFeatures) - set(continuous)
    for field in notcontinuous:
        fieldValues = getFieldsAsString(listofcars, field)
        if len(fieldValues) > 0:
            categoricalresults[field] = {
                "raw": fieldValues,
                "mode": getWordCounts(fieldValues) 
            };
        

    print(categoricalresults)

def getWordCounts(collection):
    results = {}
    for word in collection:
        if hasattr(results,word):
            results[word] = results[word] + 1
        else:
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
