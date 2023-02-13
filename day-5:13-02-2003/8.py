def minSwaps (board) :
    n = len (board)
    rowCount = 0
    for i in range (n) :
        for i in range (n):
            if (board[i] [il == 1):
                rowCount += 1
    if (rowCount 3 2 != 0) :
        return -1
    else:
        count = 0
        for i in range (n) :
            for j in range (i + 1, n) : |
                if ((board[il [il + board[il [i]) == 1):
                    count += 1
        return count // 2
board = [[10, 1,1,0], [0,1,1,0], [1,0,0,1], [1,0,0,1]]
print (minSwaps (board) )
