def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    global lst, n, r_slash, l_slash
    col=[0]*N       #設立一個list儲存每個皇后位置，index代表第幾個row，col[index]表示在這個row中的第幾個column
    lst=[]          #lst儲存最後答案
    n=N
    row = 0
    r_slash=[]
    l_slash=[]       
    dfs(row, col)    #設立一個方法來深度優先走訪各節點
    return lst

def dfs(row, col):
    if n == 0:  
        return
    while col[row] <= n-1 and row<= n-1:
        if row-col[row] not in r_slash[:row] and row+col[row] not in l_slash[:row] and col[row] not in col[:row] or row == 0:            #設立此方法來驗證是否為可設立皇后之節點
            if row == n-1:          #若走到這且row跟N-1數值一樣表示得到一個答案，跑ans方法將col裡的值轉成題目要求並存入lst
                ans(col)
            if row<n-1:             #繼續往下一個row找合適放置皇后的位置
                r_slash.append(row-col[row])    #將左右斜線加入list中以便之後判斷
                l_slash.append(row+col[row])
                dfs(row+1, col)
            if col[row] == n-1:
                col[row] = 0
                if row == 0:
                    return
                del r_slash[row-1]
                del l_slash[row-1]
                return
            col[row] += 1           #若回來這層row重新找新的位置，則從下一個column找起，避免重複走訪節點
        else:
            if col[row] == n-1:
                col[row] = 0
                del r_slash[row-1]
                del l_slash[row-1]
                return
            col[row]+=1       #若此位置被判斷會被其他皇后攻擊，則在相同row尋找下一個column
    # if col[row] == n:
    #     col[row] = 0
    #     return

# def jud(row, col):              
#     if row == 0:
#         return True
#     else:
#         for i in range(row):
#             if abs(col[row]-col[i]) == abs(row - i) or col[row] == col[i]:
#                 return False
#         return True

def ans(col):                #將得到的其中答案取出並轉換格式儲存至全域變數的lst中
    tmp_lst= []
    for i in range(n):
        a="-"
        b=a*col[i]
        b=b+"Q"
        b=b+a*(n-col[i]-1)
        tmp_lst.append(b)
    lst.append(tmp_lst)

if __name__ == '__main__':
    N = 5
    print(homework_8(N))
    # [["Q"]]
    