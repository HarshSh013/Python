class Solution:
    def solveNQueens(self, n: int):
        
        def validMove(board,row,col):
            
            # check for queens in same row
            i=col
            while i>=0:
                if board[row][i]:
                    return False
                i-=1
            
            #check for diagonal that goes toward top-left
            i=row
            j=col
            while (i>=0 and j>=0):
                if board[i][j]:
                    return False
                i-=1
                j-=1
            
            # check for diagonal that goes towards bottom-left
            i=row
            j=col
            while (i<n and j>=0):
                if board[i][j]:
                    return False
                i+=1
                j-=1
            return True
        

        def solve(board,col):

        	# if solution found i.e. all places filled
            if (col==n):
                res.append([])
                for i in range(n):
                    res[-1].append("")
                    for j in range(n):
                        if board[i][j]:
                            res[-1][-1]+="Q"
                        else:
                            res[-1][-1]+="."
                return
            
            # try for all row values of that column
            for i in range(n):
                if validMove(board,i,col):
                    board[i][col]=1
                    solve(board,col+1)
                    board[i][col]=0
            return
        
        res=[]       # to store answers
        board=[]     # create the chess board
        for i in range(n):
            board.append([])
            for j in range(n):
                board[-1].append(0)
        solve(board,0)
        board.clear()
        return res