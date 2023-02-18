def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    state = list()
        
    def is_not_under_attack(row):#確認是否在其他皇后的攻擊範圍中
        for i, r in enumerate(state):
            if r == row or i + r == len(state) + row or i - r == len(state) - row:
                return False
        else:
            return True
        
    res = list()
    def backtrack_nqueen(row=0):
        for row in range(N):
            if is_not_under_attack(row):#確認是否在其他皇后的攻擊範圍中
                state.append(row)
                if len(state) == N:
                    res.append(state[:])
                else:
                    backtrack_nqueen(row+1)#檢查下一個
                state.pop()
    
    backtrack_nqueen()
    states = ([['.' * x + 'Q' + '.' * (N-x-1) for x in state] for state in res])
    return states




if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    