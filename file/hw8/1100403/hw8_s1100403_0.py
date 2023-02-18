def homework_8(n): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    state = list()
        
    def is_not_under_attack(row):
        for i, r in enumerate(state):
            if r == row or i + r == len(state) + row or i - r == len(state) - row:
                return False
        else:
            return True
        
    res = list()
    def backtrack_nqueen(row=0):
        for row in range(n):
            if is_not_under_attack(row):
                state.append(row)
                if len(state) == n:
                    res.append(state[:])
                else:
                    backtrack_nqueen(row+1)
                state.pop()
    
    backtrack_nqueen()
    states = ([['.' * x + 'Q' + '.' * (n-x-1) for x in state] for state in res])
    return states




if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    