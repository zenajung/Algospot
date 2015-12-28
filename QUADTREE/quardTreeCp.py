index = 0
treeStr = ''

def quadTree():

    global index
    global treeStr


    c = treeStr[index]
    index += 1
    if c != 'x':
        return [c]
    else:
        lt = quadTree()
        rt = quadTree()
        lb = quadTree()
        rb = quadTree()
        '''
        ret = [c]
        ret.extend(lb)
        ret.extend(rb)
        ret.extend(lt)
        ret.extend(rt)
        #print(rt)
        return ret
        '''
        return [c]+lb+rb+lt+rt


def quadTreeStr():

    global index
    global treeStr


    c = treeStr[index]
    index += 1
    if c != 'x':
        return c
    else:
        lt = quadTree()
        rt = quadTree()
        lb = quadTree()
        rb = quadTree()
        return c+lb+rb+lt+rt








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
    import time

    start = time.time()
    for i in xrange(200000):
        treeStr = 'xxwwwbxwxwbbbwwxxxwwbbbwwwwbb'
        index = 0
        ret = ''.join(quadTree())
    print("----%s seconds ----"%(time.time()-start))


    start = time.time()
    for i in xrange(200000):
        treeStr = 'xxwwwbxwxwbbbwwxxxwwbbbwwwwbb'
        index = 0
        ret = quadTree()
    print("----%s seconds ----"%(time.time()-start))
