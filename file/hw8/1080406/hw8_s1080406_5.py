import numpy as np
def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    matrix = np.zeros((N,N))
    def check(x, y, Q_index): #確認皇后有沒有互相攻擊
            for i, j in Q_index:
                if y==j or x+y==i+j or x-y==i-j:    # 如果在對角線上，則回傳False
                    return False
            return True
    def backtrack(N, x, Q_index, mat):
            if x >= N:
                board = ['-'*j + 'Q' + '-'*(N-1-j) for i,j in Q_index]  #根據Q_index畫出皇后在棋盤上的位置
                mat.append(board)   # 加入至mat中
                return 
            
            for y in range(N):    #帶入check函數，如果不在對角線上則進入到下一層
                if check(x, y, Q_index):
                    
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
    