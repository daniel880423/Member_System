 # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
def homework_8(N: int) -> List[List[str]]:
    solutions = []
    
    board = [['-' for _ in range(N)] for _ in range(N)]
    
    def is_valid(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        for j in range(col):
            if board[row][j] == 'Q':
                return False
        
        i, j = row, col
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            if board[i][j] == 'Q':
                return False
        
        i, j = row, col
        while i > 0 and j < N-1:
            i -= 1
            j += 1
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def dfs(board, row):
        if row == N:
            solution = [''.join(row) for row in board]
            solutions.append(solution)
            return