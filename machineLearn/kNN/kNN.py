
# book 2.1.2 实施kNN分类算法

from numpy import *
import operator

def createDataSet():

    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']

    return group,labels

# k-近邻算法
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]  # 计算行数 4 , 该例子 dataset.shape 为(4,2)
    # print(tile(inX, dataSetSize))
    # print(tile(inX, (dataSetSize, 1)))
    diffMat = tile(inX,(dataSetSize,1)) - dataSet  # tile 在列方向上重复size次,行重复1次
    print(diffMat)
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)        # 按 行 相加
    distances = sqDistances **0.5
    sortedDistIndicies = distances.argsort()   # 大小排序返回索引
    classCount = {}

    for i in range(k):                         # 统计距离最近的k个点,统计每种类型出现的次数
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) +1
        print(classCount)
        print('- - - - -')
    #
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True) # 按照出现次数排序
    print('* * * * *')
    print(sortedClassCount)
    return sortedClassCount[0][0]   # 取第1个


group,labels = createDataSet()

result1 = classify0([0,0],group,labels,3)
result2 = classify0([1,1],group,labels,3)
print (result1)
print (result2)