
maxArea = 0
dataList = None
stackS = []
stackE = []


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


    return minIndex


def fence():

    global maxArea, dataList, stackS, stackE

    while(len(stackS)):
        sp,ep = stackS.pop(),stackE.pop()
        if (ep-sp) == 1:
            maxArea = max(maxArea, dataList[sp])
            continue

        #subList = dataList[sp:ep]
        #minIndex = sp + subList.index(min(subList))                   #7.3
        #print(sp,ep,minIndex)
        #(m,minIndex) = min((v,i) for i,v in enumerate(dataList))    #8.9

        #minval = min(dataList)                                              #7.4
        #minIndex = [i for i, v in enumerate(dataList) if v == minval][0]

        minIndex = findMinIndex(sp,ep)                               # 7.9

        maxArea = max(maxArea, dataList[minIndex] * (ep-sp))
        if minIndex > sp:
            stackS.append(sp)
            stackE.append(minIndex)


        if minIndex < (ep-1):
            stackS.append(minIndex+1)
            stackE.append(ep)
        continue

    return


def fenceStr(dataStr):

    global maxArea,dataList,stackS,stackE

    maxArea = 0
    dataList = map(int,dataStr.split(' '))
    stackS = [0]
    stackE = [len(dataList)]
    #dataList = list(dataStr)
    #print(dataList)
    fence()
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
