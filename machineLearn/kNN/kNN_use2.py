
# book 2.3 示例 手写识别系统

fileName = '/Users/lawrence/Desktop/Python/machineLearn/Source/machinelearninginaction/Ch02/testDigits'
from numpy import *
from os import listdir
from kNN import classify0
# 识别数字0-9

# 将图像格式的文件转换为分类器使用的向量格式
def img2vector(file):

    returnVect = zeros((1,1024))

    fr = open(file)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])

    return returnVect


# 手写数字识别系统的测试代码
def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir(fileName)           #load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector(fileName + '/' + fileNameStr)
    testFileList = listdir(fileName)        #iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector(fileName + '/' + fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print ("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): errorCount += 1.0
    print ("\nthe total number of errors is: %d" % errorCount)
    print ("\nthe total error rate is: %f" % (errorCount/float(mTest)))


# testVector = img2vector(fileName+'/0_13.txt')

#
handwritingClassTest()