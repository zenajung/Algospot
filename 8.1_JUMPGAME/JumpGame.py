

available = None
data = None
len = 0

def jumpGame(i,j):

    global available,data,len

    if i == len-1 and j== len-1 :
        return True

    #print(i,j,data[i][j],available)
    if available[i][j] == 0:
        return False

    v = data[i][j]
    
    if i+v < len:
        if jumpGame(i+v,j):
            return True

    if j+v < len:
        if jumpGame(i,j+v):
            return True
    #print(i,j)
    available[i][j] = 0
    return False


def jumpGameStr(n,dataStrList):

    global available,data,len

    available = [[-1]*n for x in xrange(n)]


    #print(available)
    len = n
    data = []
    for dataStr in dataStrList:
        dataList = map(int,dataStr.split(' '))
        data.append(dataList)



    if jumpGame(0,0):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':

    '''
    tc = int(raw_input())
    for i in xrange(tc):
        dataStr=[]
        n = int(raw_input())
        for j in xrange(n):
            dataStr.append(raw_input())

        print(jumpGameStr(n,dataStr))


    '''

    print(jumpGameStr(7,['2 5 1 6 1 4 1','6 1 1 2 2 9 3','7 2 3 2 1 3 1','1 1 3 1 7 1 2','4 1 2 3 4 1 2','3 3 1 2 3 4 1','1 5 2 9 4 7 0']))
    print(jumpGameStr(7,['2 5 1 6 1 4 1','6 1 1 2 2 9 3','7 2 3 2 1 3 1','1 1 3 1 7 1 2','4 1 2 3 4 1 3','3 3 1 2 3 4 1','1 5 2 9 4 7 0']))


