import sys
import math


def quantize(s, n, groupNum):

    global cache

    minValue = sys.maxint


    #print(s,n,groupNum)
    if groupNum <= 1:
        #print(cache[s][n-1])
        return cache[s][n-1]

    for i in xrange(1,n-groupNum+2):

        #print('i=',i,'b minValue :' , minValue)
        if cache[s][i-1] < minValue:
            minValue  = min(minValue, cache[s][i-1] + quantize(s+i,n-i,groupNum-1))
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
    global cache
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

    print("----%s seconds ----"%(time.time()-start))
    return quantize(0,n,groupNum)



if __name__ == '__main__':

    '''
    tc = int(raw_input())
    for i in xrange(tc):
        numStr = raw_input()
        dataStr = raw_input()

        print(quantizeStr(numStr,dataStr))


    '''

    #print(quantizeStr('10 3','3 3 3 1 2 3 2 2 2 1'))
    #print(quantizeStr('9 3','1 744 755 4 897 902 890 6 777'))

    import time

    global start
    start = time.time()
    for i in xrange(1):
        print(quantizeStr('40 10','1 744 755 4 897 902 890 6 777 2 775 776 5 877 999 892 8 7888 7 999 1 744 755 4 897 902 890 6 777 2 775 776 5 877 999 892 8 7888 7 999'))

    print("----%s seconds ----"%(time.time()-start))

    # 20 : 3.36 -> 200: 3.4   10.9
