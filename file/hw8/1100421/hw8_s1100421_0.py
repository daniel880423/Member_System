def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    col=[0]*N       #設立一個list儲存每個皇后位置，index代表第幾個row，col[index]表示在這個row中的第幾個column
    global lst      #lst儲存最後答案
    lst=[]
    row = 0         
    dfs(row, col, N)    #設立一個方法來深度優先走訪各節點
    return lst

def dfs(row, col, N):
    if N == 0:  
        return
    while col[row] <= N-1 and row<=N-1:         
        if jud(row,col):            #設立此方法來驗證是否為可設立皇后之節點
            if row == N-1:          #若走到這且row跟N-1數值一樣表示得到一個答案，跑ans方法將col裡的值轉成題目要求並存入lst
                ans(col, N)
            if row<N-1:             #繼續往下一個row找合適放置皇后的位置
                dfs(row+1, col, N)
            col[row] += 1           #若回來這層row重新找新的位置，則從下一個column找起，避免重複走訪節點
        else:
            col[row] +=1            #若此位置被判斷會被其他皇后攻擊，則在相同row尋找下一個column
    if col[row] == N:               #此條件成立，代表這個row的所有column都已經走訪完且沒有找到適合的點，將col[row]重置，並往上一個row繼續走訪
        col[row] = 0
        return

def jud(row, col):              #判斷此節點若是設置皇后會不會被攻擊
    if row == 0:
        return True
    else:
        for i in range(row):
            if abs(col[row]-col[i]) == abs(row - i) or col[row] == col[i]:
                return False
        return True

def ans(col, N):                #將得到的其中答案取出並轉換格式儲存至全域變數的lst中
    tmp_lst=[]
    for i in range(N):
        a="-"
        b=a*col[i]
        b=b+"Q"
        b=b+a*(N-col[i]-1)
        tmp_lst.append(b)
    lst.append(tmp_lst)

if __name__ == '__main__':
    N = 5
    print(homework_8(N))
    # [["Q"]]
    