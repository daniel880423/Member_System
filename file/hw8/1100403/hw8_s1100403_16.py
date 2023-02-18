def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    ans = []                                                        # result
    row = []                                                        # 列
    col = [False] * N                                               # 行
    slash1 = [False] * (2 * N - 1)                                  # 斜線1
    slash2 = [False] * (2 * N - 1)                                  # 斜線2
    if N==0:
        return ans
    putQueen(N, 0, row, ans, col, slash1, slash2)
    return ans

def putQueen(n, index, row, ans, col, slash1, slash2):
    if index == n:                                                                  #i行
        ans.append(create(n, row))
        return
    for i in range(n):                                                              #列
        if not col[i] and not slash1[index+i] and not slash2[index-i+(n-1)]:        #沒有存在其他皇后
            row.append(i)                                                           #放入新皇后
            col[i] = True   
            slash1[index+i] = True  
            slash2[index - i + (n - 1)] = True                                      #行、斜線True
            putQueen(n, index+1, row, ans, col, slash1, slash2)                     #進入下一層遞迴
            col[i] = False                                                          #沒有找到可以放置新皇后的位置則移除
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
    N = 1
    print(homework_8(N))
    # [["Q"]]
    