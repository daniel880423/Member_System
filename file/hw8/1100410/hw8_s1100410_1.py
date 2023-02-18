def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    if N==0:                        #如果N=0
        return([])                  #直接回傳空list

    global col, check_Column, check_Right_slash, check_Left_slash, position #定義所需全域變數
    col = [[0]*N for i in range(N)] #col為N*N矩陣
    check_Column=[]                 #會放當前皇后column位置，用來判斷下個皇后是否在同一行
    check_Right_slash=[]            #會放當前皇后row-column位置，用來判斷下個皇后是否在同一右斜線
    check_Left_slash=[]             #會放當前皇后row+column位置，用來判斷下個皇后是否在同一左斜線
    position = []                   #放最終皇后位置答案
    queens(0,N)                     #進入queens function，從第0行開始跑
    
    #以下用來將答案轉為指定格式
    ans =[[]*N for i in range(len(position))]#答案中會有len(position)(位置答案組合數量)個list，每個答案包含1個"Q"和N-1個"-"
    for i in range(len(position)):           #看有幾組位置答案組合，就要跑幾次
        for j in range(N):                   #一個位置答案，有N個皇后位置，所以要執行N次
            str = "-"*(N-1)                  #設str初值為N-1個"-"
            new_s = str[:position[i][j]] + 'Q' + str[position[i][j]:] #new_s為原str加上指定位置的'Q'
            ans[i].append(new_s)             #將new_s加進ans中
    return ans                               #回傳ans

def queens(s,N):
    #如果s跑到N代表全部皇后位置都確定了(因為我們是從0開始跑，跑到N-1就有N個皇后位置了)
    if s==N:
        position.append(check_Column[:])    #將這組皇后位置答案加到position裡

    #如果s是0~N-1，存取皇后位置(要判斷跟前面皇后位置的相對位置)
    else:
        for j1 in range(N):                 #j1為第s列皇后的column值，可從0~N
            #如果跟前面的皇后不在同一行、同一右斜線和同一左斜線
            if (j1 not in check_Column) and (s-j1 not in check_Right_slash) and (s+j1 not in check_Left_slash):
                check_Column.append(j1)         #放當前皇后column位置
                check_Right_slash.append(s-j1)  #放當前皇后row-column位置
                check_Left_slash.append(s+j1)   #放當前皇后row+column位置
                queens(s+1,N)                   #進入下一列的皇后
                check_Column.pop()              #刪除剛剛放的當前皇后column位置
                check_Right_slash.pop()         #刪除剛剛放的放當前皇后row-column位置
                check_Left_slash.pop()          #刪除剛剛放的放當前皇后row+column位置

            elif j1==N-1:                     #如果在找到最後一行，還是找不到可以放的位置
                break                       #直接break，回到上一層遞迴

            
                
if __name__ == '__main__':
    N = 2
    print(homework_8(N))
    # [["Q"]]
    