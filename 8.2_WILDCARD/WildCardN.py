

def wildCard( gFilter, gTarget):

    lTarget = len(gTarget)
    lFilter = len(gFilter)
    tCacheOld = [False for _ in xrange(lTarget+1)]
    tCacheOld[0] = True

    for fIndex in xrange(1,lFilter+1):
        tCacheNew = []
        c = gFilter[fIndex-1]
        if c == '*' or c == '?':
            tCacheNew.append(tCacheOld[0])
        else:
            tCacheNew.append(False)

        for tIndex in xrange(1,lTarget+1):
            if c == '*':
                tCacheNew.append(tCacheOld[tIndex] or tCacheNew[tIndex-1])
            elif c == '?':
                tCacheNew.append(tCacheOld[tIndex-1])
            else:
                tCacheNew.append(tCacheOld[tIndex-1] and c == gTarget[tIndex-1])

        tCacheOld = tCacheNew


    return tCacheNew[lTarget]






def wildCardStr(pFilter, n, exList):

    successList = []

    for i in xrange(n):
        gFilter = pFilter
        gTarget = exList[i]


        if wildCard(gFilter, gTarget) :
            successList.append(exList[i])

    if len(successList) > 1 :
        successList.sort()


    return '\n'.join(successList)



if __name__ == '__main__':


    tc = int(raw_input())
    for i in xrange(tc):
        dataStr=[]

        pFilter = raw_input()
        n = int(raw_input())
        for j in xrange(n):
            dataStr.append(raw_input())

        print(wildCardStr(pFilter,n,dataStr))


    '''

    print(wildCardStr('he?p',3,['help','heap','helpp']))
    print(wildCardStr('*p*',3,['help','papa','hello']))
    print(wildCardStr('*bb*',1,['babbbc']))
    print(wildCardStr('t*l?*o*r?ng*s',1,['thelordoftherings']))

    '''