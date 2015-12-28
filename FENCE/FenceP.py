
maxArea = 0
dataList = None


import sys
def findMinIndex(sp,ep):

    global dataList

    minValue = sys.maxint
    minIndex = -1;
    for i in xrange(sp,ep):
        v = dataList[i]

        if minValue > v:
            minValue = v
            minIndex = i

        #(minValue,minIndex) = min((v,i),(minValue,minIndex))

    return minIndex


def fence(sp,ep):

    global maxArea, dataList

    if ep-sp == 1:
        maxArea = max(maxArea, dataList[sp])
        return

    #subList = dataList[sp:ep]
    #minIndex = sp+ subList.index(min(subList))                   #6.0

    #(m,minIndex) = min((v,i) for i,v in enumerate(dataList))    #8.9

    #minval = min(dataList)                                              #7.4
    #minIndex = [i for i, v in enumerate(dataList) if v == minval][0]

    minIndex = findMinIndex(sp,ep)                               # 6.04

    maxArea = max(maxArea, dataList[minIndex] * (ep-sp))
    if minIndex > sp:
        fence(sp,minIndex)

    if minIndex < (ep-1):
        fence(minIndex+1,ep)
    return


def fenceStr(dataStr):

    global maxArea,dataList

    maxArea = 0
    dataList = map(int,dataStr.split(' '))
    #dataList = list(dataStr)
    #print(dataList)
    fence(0,len(dataList))
    return str(maxArea)


if __name__ == '__main__':

    '''
    tc = int(raw_input())
    for i in xrange(tc):

        raw_input()
        dataStr = raw_input()

        print(fenceStr(dataStr))


    '''

    print(fenceStr('7 1 5 9 6 7 3'))
    print(fenceStr('1 4 4 4 4 1 1'))
    print(fenceStr('1 8 2 2'))

    import time

    start = time.time()
    for i in xrange(80000):
        fenceStr('7 1 5 9 6 7 3 50 23 1 8 33 55 3 2 5 23 3 22 33 34 53 63 2 3 63 34 23 23 33')


    print("----%s seconds ----"%(time.time()-start))


    # 5.8 sec
