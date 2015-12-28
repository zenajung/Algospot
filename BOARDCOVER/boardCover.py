__author__ = 'zena'


def findCover(row,column,map, n):

    if numOfSpace(row,column,map) == 0:
        return n+1;

    for i in xrange(row):
        for j in xrange(column):
            if map[j][i] == '.' :
                if j>1 and map[j-1][i] == '.' and i>1 and map[j][i-1] == '.' :
                    map[j-1] = '#'
                    map[i-1] = '#'
                    findCover(row,column,map,n)







def boardCover(row,column,map):



    return 1





if __name__ == '__main__':

    '''
    tc = int(raw_input())
    for i in xrange(tc):
        ln = raw_input()
        ln_list = ln.split()
        n = int(ln_list[0])
        m = int(ln_list[1])
        matrix = []
        for j in xrange(n):
            lm = raw_input()
            lm_list = lm.split()
            mdata = [int(x) for x in lm_list]
            matrix.append(mdata)

        print(Cleaner(n,m,matrix))

    '''

    matrix = [['#','.','.','.','.','.','#'],['#','.','.','.','.','.','#'],['#','#','.','.','#','#','#']]

    print(boardCover(3,7,matrix))