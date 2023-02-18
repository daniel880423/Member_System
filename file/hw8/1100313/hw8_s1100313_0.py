def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    global ans
    ans=[]
    def promising(row, col, right_slash, left_slash):
        if N==0:                                                                         #若N=0，直接回傳[]
            return []
        global ans
        if row==N:                                                                       #row==N，代表有解，開始排Q的位置
            stack=[["-"]*N for i in range(N)]
            for i in range(N):
                stack[i][col[i]]="Q"                                       
                stack[i]="".join(stack[i])
            ans.append(stack)
  
        for i in range(N):
            if i not in col and row-i not in right_slash and  row+i not in left_slash:  #若列，又斜線和左斜線都沒有皇后
                promising(row+1, col+[i], right_slash+[row-i], left_slash+[row+i])      #放置皇后，並記錄它的位置，繼續跑下一行
    promising(0, [], [], [])                                                            #呼叫函式

    return ans

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    