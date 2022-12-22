import numpy as np
import operator
import sys
from os import listdir

def createDataSet(directory_name):
    labels = []
    file_list = listdir(directory_name)
    m = len(file_list)
    returnMat = np.zeros((m, 1024))

    for i in range(m):
        labels.append(int(file_list[i].split('_')[0]))
        returnMat[i, :] = fileToVector(directory_name + '/' + file_list[i])
    return returnMat, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
                              key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def fileToVector(filename):
    listFromLine = []
    with open(filename) as f:
        for line in f.readlines():
            line = list(str.strip(line))
            listFromLine.append(line)
    arrFromList = np.array(listFromLine, int)
    returnVector = np.reshape(arrFromList, (1, 1024))
    return returnVector

trainingDigits = sys.argv[1]
testDigits = sys.argv[2]

matrix, labels = createDataSet(trainingDigits)

test_file_list = listdir(testDigits)
m = len(test_file_list)

for k in range(1, 21):
    count = 0
    errorCount = 0

    for i in range(m):
        answer = int(test_file_list[i].split('_')[0])
        testArray = fileToVector(testDigits + '/' + test_file_list[i])
        classifiedResult = classify0(testArray, matrix, labels, k)

        count += 1
        if answer != classifiedResult:
            errorCount += 1

    print(int(errorCount / count * 100))
