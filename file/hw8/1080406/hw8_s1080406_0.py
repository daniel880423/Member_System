import numpy as np
def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    matrix = np.zeros((N,N))
    def check( x, y, Q_index):
            for i, j in Q_index:
                if y==j or x+y==i+j or x-y==i-j:    # check column and diagnal
                    return False
            return True
    def backtrack(N, x, Q_index, mat):
            '''
            x: row index
            Q_index: a list of currently added Qs
            '''
            if x >= N:
                board = ['.'*j + 'Q' + '.'*(N-1-j) for i,j in Q_index]  # create a board according to Q_index
                mat.append(board)   # add the board to result list 
                return 
            # try possible positions at this row
            for y in range(N):
                if check( x, y, Q_index):
                    # add (x,y) to Q_index and treat the next row
                    backtrack(N, x+1, Q_index+[(x,y)], mat) 
            return 
    if N > 9 or N < 1:
        return []   
    if N == 1:
        return [['Q']]
    elif N <=3:
        return []
    res = []
    backtrack(N, 0, [], res)
        
    return res
        



if __name__ == '__main__':
    N = 5
    print(homework_8(N))
    # [["Q"]]
    