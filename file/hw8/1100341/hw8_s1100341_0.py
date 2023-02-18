def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking

    global ans
    ans = []
    if N == 0:
        return ans
    def A (N, row, colum, rs, ls):    #建一個皇后在的function
        
        global ans
        if row == N:                  
            lst = []
            for i in colum:      
                s = ''
                for j in range(N):
                    if i == j:     #i=算出來的皇后位置時
                        s += 'Q'   #放Q
                    else:
                        s += '-'   #其他放-
                lst.append(s)

            ans.append(lst)   #把lst append到ans裡
                
        for i in range(N):
            if i not in colum and row-i not in rs and row+i not in ls:    #如果i在有皇后的位置的話

                A(N, row+1, colum+[i], rs+[row-i], ls+[row+i])   #呼叫紀錄有皇后的位置的下一個

    A (N, 0, [], [], [])





    return ans

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    