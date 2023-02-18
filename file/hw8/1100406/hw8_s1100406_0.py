def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    res = []            
    row = []            
    col = [False] * N   
    slash1 = [False] * (2 * N - 1) 
    slash2 = [False] * (2 * N - 1) 
    if N==0:
        return res
    putQueen(N, 0, row, res, col, slash1, slash2)
    return res

def putQueen(n, index, row, res, col, slash1, slash2):
    if index == n:  
        res.append(create(n, row))
        return
    for i in range(n):  
        if not col[i] and not slash1[index+i] and not slash2[index-i+(n-1)]:
            row.append(i)   
            col[i] = True   
            slash1[index+i] = True  
            slash2[index - i + (n - 1)] = True  
            putQueen(n, index+1, row, res, col, slash1, slash2) 
            col[i] = False          
            slash1[index + i] = False
            slash2[index - i + (n - 1)] = False
            row.pop()
    return

def create(n, row):
    if len(row) != n:
        return False
    board = [["-"] * n for k in range(n)]
    for i in range(n):
        board[i][row[i]] = "Q"
        board[i] = "".join(board[i])
    return board



if __name__ == '__main__':
    N = 0
    print(homework_8(N))
    # [["Q"]]
    