__author__ = 'zena'

'''
def quadTree(treeList):

    #if(x in tree[1:] == False):
    tree = []
    index = 0;
    for i in xrange(4):
        print(index,treeList[index])
        if treeList[index+1] == 'x' :
            j,t = quadTree(treeList[index+1:])
            tree.append(t)
            index += j
        else:
            tree.append(treeList[index+1])
            index+=1

    return index+1,tree;

def swapTree(tree):
    for i in xrange(4):
        if type(tree[i]) is list:
            swapTree(tree[i])
    tree[0],tree[1],tree[2],tree[3] = tree[2],tree[3],tree[0],tree[1]
'''
def treeToStr(tree):
    #print(tree)
    for i in xrange(4):
        if type(tree[i]) is list:
            tree[i] = treeToStr(tree[i])
    #print(tree)
    return 'x' + ''.join(tree)



def quadTree(treeList):

    tree = []
    index = 0;

    for i in xrange(4):
        #print(index,treeList[index])
        if treeList[index+1] == 'x' :
            j,t = quadTree(treeList[index+1:])
            tree.append(t)
            index += j
        else:
            tree.append(treeList[index+1])
            index+=1
    tree[0],tree[1],tree[2],tree[3] = tree[2],tree[3],tree[0],tree[1]


    return index+1,tree;

def quadTreeStr(treeStr):

    if len(treeStr) == 1:
        return treeStr

    treeList = list(treeStr)
    #return treeList
    i,tree = quadTree(treeList)
    #print(tree)
    #swapTree(tree)
    #print(tree)

    return treeToStr(tree)
    #return tree
    #treeStr = ''.join(treeArray)



if __name__ == '__main__':


    tc = int(raw_input())
    for i in xrange(tc):
        treeStr = raw_input()

        print(quadTreeStr(treeStr))

    '''
    treeStr = 'w'
    #treeStr = 'xbwwb'

    #treeStr = 'xxbwwbbbw'

    #treeStr = 'xbwxwbbwb'
    #treeStr = 'xxwwwbxwxwbbbwwxxxwwbbbwwwwbb'


    print(quadTreeStr(treeStr))
    '''