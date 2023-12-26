#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
import operator
import os
import sys
    
def createDataSet(foldername):
    labels = []
    fileList = os.listdir(foldername)
    m = len(fileList)
    matrix = np.zeros((m, 1024)) # 반환된 vector를 담을 곳

    for i in range(m): 
        fileNameData = fileList[i]
        labels.append(int(fileNameData.split('_')[0])) 
        matrix[i, :] = getVector(foldername + '/' + fileNameData)
    return matrix, labels 

# def autoNorm(dataSet):
#     minVals = dataSet.min(0)
#     maxVals = dataSet.max(0)
#     ranges = maxVals - minVals
#     normDataSet = np.zeros(np.shape(dataSet))
#     m = dataSet.shape[0]
#     normDataSet = dataSet - np.tile(minVals, (m, 1))
#     normDataSet = normDataSet / np.tile(ranges, (m, 1))
#     return normDataSet, ranges, minVals

def getVector(filename): 
    vector = np.zeros((1, 1024)) 
    with open(filename) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line[j])
        return vector   

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


if __name__ == "__main__":
    
    trainingDataFolderName = sys.argv[1]
    testDataFolderName = sys.argv[2]
    
    testFileList = os.listdir(testDataFolderName)
    length = len(testFileList)

    matrix, labels = createDataSet(trainingDataFolderName)
    
    for k in range(1, 21): 
        count = 0 
        errorCount = 0 
        for i in range(length): 
            answer = int(testFileList[i].split('_')[0])
            testData = getVector(testDataFolderName + '/' + testFileList[i])
            classifiedResult = classify0(testData, matrix, labels, k)
        
            count += 1
            if answer != classifiedResult :
                errorCount += 1
        print(int(errorCount / count * 100))

