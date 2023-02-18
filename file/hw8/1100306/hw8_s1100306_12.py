def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    res = []
    cur = [['-'] * N for _ in range(N)]
    
    def backtracking(n, row, cur, res):
        if row == n:
            res.append([''.join(cur[i]) for i in range(n)])
            return 
        
        for j in range(n):
            if not is_valid(row, j, cur):
                continue
            cur[row][j] = 'Q'
            backtracking(n, row + 1, cur, res)
            cur[row][j] = '-'
    
    
    def is_valid(m, n, cur):
        for i in range(m):
            if cur[i][n] == 'Q':
                return False
            if n + m - i < len(cur) and cur[i][n + m - i] == 'Q':
                return False
            if n - m + i >= 0 and cur[i][n - m + i] == 'Q':
                return False
        
        return True
	
    backtracking(N, 0, cur, res)
    if N == 0:
        return []
    return res
if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    