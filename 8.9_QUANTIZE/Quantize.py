import sys
import math

qCache = []
numOfList = 0

def quantize(s, groupNum):

    global cache,qCache, numOfList
    n = numOfList-s-groupNum+1
    #print('--', s,n,groupNum)

    minValue = sys.maxint


    #print(s,n,groupNum)
    if groupNum <= 1:
        #print(cache[s][n-1])
        return cache[s][n-1]

    if qCache[s][groupNum] == -1 :
    #if True:
        for i in xrange(1,n):

            #print('i=',i,'b minValue :' , minValue)
            '''
            if cache[s][i-1] < minValue:
                minValue  = min(minValue, cache[s][i-1] + quantize(s+i,n-i,groupNum-1))
            '''
            minValue  = min(minValue, cache[s][i-1] + quantize(s+i,groupNum-1))
        #'''
        #if qCache[s][groupNum] != -1 and qCache[s][groupNum] != minValue:
        #    print(s,n,qCache[s][n],minValue)
        #'''
        #print(s,n,qCache[s][groupNum],minValue)
        qCache[s][groupNum] = minValue;

    return qCache[s][groupNum]

        #print('a minValue :' , minValue)
    #print(s,n,groupNum,minValue)
    return minValue


def quantizeStr(nStr,dataStr):

    global start

    numList = map(int, nStr.split())
    n = numList[0]
    groupNum = numList[1]
    dataList = map(int,dataStr.split())

    dataList.sort()
    #print(dataList)
    sumList = [0]*(n+1)
    for i in xrange(0,n):
        sumList[i+1] = sumList[i] + dataList[i]

    #print(sumList)
    global cache, qCache, numOfList
    cache = []

    for s in xrange(n):
        #d = dataList[s]
        minList= []
        for num in xrange(1,n-s+1):
            #sumValue = sumList[s+num] - sumList[s]
            mean = int(float(sumList[s+num] - sumList[s])/float(num) + 0.5)

            minValue = 0
            for i in xrange(s,s+num):
                #print('i:',i)
                #minValue = minValue + (dataList[i]-mean)*(dataList[i]-mean)
                minValue += (dataList[i]-mean)**2
            '''
            minValue = sum( (v-mean)*(v-mean) for v in dataList[s:s+num] )
            '''
            #minValue = sum(i*i for v in dataList[s:s+num])
            #print('sum :',sum,'mean :',mean,'minValue :',minValue)
            minList.append(minValue)
        cache.append(minList)


    #print(cache)

    qCache = [[-1]*(n+1) for _ in xrange(n+1)]


    #print("----%s seconds ----"%(time.time()-start))
    numOfList = n
    return quantize(0,groupNum)



if __name__ == '__main__':


    tc = int(raw_input())
    for i in xrange(tc):
        numStr = raw_input()
        dataStr = raw_input()

        print(quantizeStr(numStr,dataStr))


    '''

    print(quantizeStr('10 3','3 3 3 1 2 3 2 2 2 1'))
    print(quantizeStr('9 3','1 744 755 4 897 902 890 6 777'))

    import time

    global start
    start = time.time()
    for i in xrange(1):
        #print(quantizeStr('40 20','1 744 755 4 897 902 890 6 777 2 775 776 5 877 999 892 8 7888 7 999 1 744 755 4 897 902 890 6 777 2 775 776 5 877 999 892 8 7888 7 999'))
        print(quantizeStr('20 9','1 744 755 4 897 902 890 6 777 300 27 53 441 7 88 93 63 22 873 92'))
        #print(quantizeStr('6 4','1 2 3 4 8 9'))
    print("----%s seconds ----"%(time.time()-start))

    # 20 : 3.36 -> 200: 3.4   10.9
    # 10 179058 , 56
    '''