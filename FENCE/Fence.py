
maxArea = 0
import sys
def findMinIndex(dataList):
    minValue = sys.maxint
    minIndex = -1;
    for i,v in enumerate(dataList):
        if minValue > v:
            minValue = v
            minIndex = i


    return minIndex


def fence(dataList):

    global maxArea
    '''
    if len(dataList) == 1:
        maxArea = max(maxArea, dataList[0])
        return
    '''

    minIndex = dataList.index(min(dataList))                   #5.8
    #(m,minIndex) = min((v,i) for i,v in enumerate(dataList))    #8.9

    #minval = min(dataList)                                              #7.4
    #minIndex = [i for i, v in enumerate(dataList) if v == minval][0]

    #minIndex = findMinIndex(dataList)                               # 6.8
    dataLen = len(dataList)
    maxArea = max(maxArea, dataList[minIndex] * dataLen)
    if minIndex == 1:
        maxArea = max(maxArea, dataList[0])

    if minIndex == (dataLen-2) :
        maxArea = max(maxArea, dataList[dataLen-1])


    if minIndex > 1:
        fence(dataList[:minIndex])

    if minIndex < (len(dataList)-2):
        fence(dataList[minIndex+1:])
    return


def fenceStr(dataStr):

    global maxArea

    maxArea = 0
    dataList = map(int,dataStr.split(' '))
    #dataList = list(dataStr)
    #print(dataList)
    if(len(dataList) == 1):
        return str(dataList[0])
    fence(dataList)
    return str(maxArea)


if __name__ == '__main__':

    '''
    tc = int(raw_input())
    for i in xrange(tc):
        index = 0
        treeStr = raw_input()

        print(''.join(quadTree()))



    #treeStr = 'w'
    #treeStr = 'xbwwb'

    #treeStr = 'xxbwwbbbw'

    #treeStr = 'xbwxwbbwb'
    treeStr = 'xxwwwbxwxwbbbwwxxxwwbbbwwwwbb'

    print(''.join(quadTree()))
    '''

    print(fenceStr('7 1 5 9 6 7 3'))
    print(fenceStr('1 4 4 4 4 1 1'))
    print(fenceStr('1 8 2 2'))

    import time

    start = time.time()
    for i in xrange(20000):
        fenceStr('7 1 5 9 6 7 3 50 23 1 8 33 55 3 2 5 23 3 22 33 34 53 63 2 3 63 34 23 23 33 7 1 5 9 6 7 3 50 23 1 8 33 55 3 2 5 23 3 22 33 34 53 63 2 3 63 34 23 23 33 7 1 5 9 6 7 3 50 23 1 8 33 55 3 2 5 23 3 22 33 34 53 63 2 3 63 34 23 23 33 7 1 5 9 6 7 3 50 23 1 8 33 55 3 2 5 23 3 22 33 34 53 63 2 3 63 34 23 23 33')


    print("----%s seconds ----"%(time.time()-start))


    # 5.8 sec