
def trianglePath(dataLen,dataList):

    #dataLen = len(dataList)
    oldCache = dataList.pop()

    for i in xrange(dataLen-1):
        newCache = []
        data = dataList.pop()
        for j in xrange(len(data)):
            newCache.append(data[j] + max(oldCache[j], oldCache[j+1]))
        oldCache = newCache

    return oldCache[0]


def trianglePathStr(n,dataStrList):

    data = []
    for dataStr in dataStrList:
        dataList = map(int,dataStr.split())
        data.append(dataList)


    return trianglePath(n, data)



if __name__ == '__main__':


    tc = int(raw_input())
    for i in xrange(tc):
        dataStr=[]
        n = int(raw_input())
        for j in xrange(n):
            dataStr.append(raw_input())

        print(trianglePathStr(n,dataStr))


    '''

    print(trianglePathStr(5,['6','1  2','3  7  4','9  4  1  7','2  7  5  9  4']))
    print(trianglePathStr(5,['1','2 4','8 16 8','32 64 32 64','128 256 128 256 128']))
    '''

