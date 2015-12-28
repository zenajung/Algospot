
gFilter = None
gTarget = None

gCache = None

def wildCard( iFilter, iTarget):

    global gFilter, gTarget, gCache

    if iFilter < -1 or iTarget < -1 :
        return False

    if (iFilter == 0 and iTarget == 0) or (iFilter == -1 and iTarget ==  -1) :
        return True

    cache = gCache[iFilter+1][iTarget+1]
    if  cache != -1:
        return  cache

    c = gFilter[iFilter]

    if c == '*' :
        gCache[iFilter+1][iTarget+1] =  wildCard(iFilter-1,iTarget) or wildCard(iFilter, iTarget-1)


    elif c == '?':
        gCache[iFilter+1][iTarget+1] = wildCard(iFilter-1, iTarget-1)

    else :
        gCache[iFilter+1][iTarget+1] = wildCard(iFilter-1, iTarget-1) and c == gTarget[iTarget]


    return gCache[iFilter+1][iTarget+1]






def wildCardStr(pFilter, n, exList):

    global gFilter, gTarget, gCache
    successList = []

    for i in xrange(n):
        gFilter = pFilter
        gTarget = exList[i]

        gCache = [ [-1] * (len(gTarget)+1) for _ in  xrange(len(gFilter)+1) ]

        if wildCard(len(gFilter)-1, len(gTarget)-1) :
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