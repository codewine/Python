
# book 2.2 实施kNN分类算法

from numpy import *
import operator
import random
from kNN import classify0

DataFileName = 'data.text'
DataFileName = '/Users/lawrence/Desktop/Python/machineLearn/Source/machinelearninginaction/Ch02/datingTestSet2.txt'

# 生成随机原始数据
def getData():

    with open('data.text','a',encoding='utf-8') as file:

        for i in range(1000):
            flight = random.randint(1, 10000)
            game = random.randint(1, 25)
            icecream = random.uniform(0,2)
            like = random.randint(1, 3)
            data = "{},{},{},{}\n".format(flight, game, icecream,like)

            file.write(data)

# 将文本记录转换为NumPy的解析程序
def file2matrix(filename):
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberofLines = len(arrayOfLines)
    returnMat = zeros((numberofLines,3))   #创建返回的numpy矩阵
    classLabelVector = []
    index = 0
    for line in arrayOfLines:  #解析文件数据到列表
        line = line.strip()
        # listFormLine = line.split(',') # data.text中使用","号分割
        listFormLine = line.split('\t')
        returnMat[index,:] = listFormLine[0:3]
        classLabelVector.append(int(listFormLine[-1]))
        index +=1

    return returnMat,classLabelVector



# 使用matplotlib创建散点图
def showMatplotlib():
    import matplotlib
    import matplotlib.pyplot as plt

    # 获取数据
    datingDataMat, datingLabels = file2matrix(DataFileName)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 不设置色彩
    # ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
    # 设置色彩
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
    plt.show()

# 归一化特征值 ,合理权重
def autoNorm(dataSet):
    # 获取数据
    minVals = dataSet.min(0) #(比较牛逼,n组数据中,可以返回每组数据的每个index元素的最小值,组合成一个组)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))   # 扩展矩阵函数tile  old - min
    normDataSet = normDataSet/tile(ranges,(m,1))  #特征值相除
    return normDataSet,ranges,minVals


# 测试算法:作为完整程序验证分类器
def datingClassTest():

    hoRatio = 0.5
    # 获取数据
    datingDataMat, datingLabels = file2matrix(DataFileName)
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):

        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print ('the classfifier came back with: %d,the real answer is: %d'%(classifierResult,datingLabels[i]))

        if (classifierResult != datingLabels[i]):errorCount +=1.0

    print('the total error rate is: %f'%(errorCount/float(numTestVecs)))

# 约会网站预测函数

def classifyPerson():

    resultList = ['not at all','in small doses','in large doses']
    percentTats = float(input('perchentage of time spent playing video games?'))
    ffMiles = float(input('frequent flier miles eraned  per year?'))
    iceCream = float(input('liters of ice cream consumed per year?'))

    datingDataMat, datingLabels = file2matrix(DataFileName)
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])

    classifyResult =  classify0((inArr - minVals)/ranges,normMat,datingLabels,3)

    print ('you will probable like this person:',resultList[classifyResult -1])



#
classifyPerson()