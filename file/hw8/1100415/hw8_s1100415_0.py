def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if N == 0:                                                              #如果N=0 回傳空矩陣
        return []

                                                                            #設立三集合
    col = set()                                                             #直行
    rightdiag = set()                                                       #右上斜線
    leftdiag = set()                                                        #左上斜線

    result = []                                                             
    board = [["-"] * N for i in range(N)]                                   #依照N建立棋盤

    def backtrack(r):
        if r == N:                                                          #測試每一列可以皇后可能
            copy = ["".join(row) for row in board]                          #將答案複製(string方式)
            result.append(copy)                                             #加入result中
            return
        
        for c in range(N):                                                  #利用皇后的直行、兩對角線 檢查皇后位置是否正確    
            if c in col or (r + c) in rightdiag or (r-c) in leftdiag:       
                continue


            col.add(c)                                                      #更新三集合
            rightdiag.add(r + c)
            leftdiag.add(r - c)
            board[r][c] = "Q"                                               #更新棋盤

            backtrack(r + 1)                                                

            col.remove(c)                                                   #更新三集合
            rightdiag.remove(r + c)
            leftdiag.remove(r - c)                                             
            board[r][c] = "-"                                               #更新棋盤

    backtrack(0)
    return(result)
if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    