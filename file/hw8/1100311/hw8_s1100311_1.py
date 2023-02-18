def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    global ans 
    ans = []                                  # 設一個放答案的空list
    if N == 0:                                #如果N = 0 沒有棋盤，所以直接輸出答案
        return ans

    def deep(n,row,col,r_sl,l_sl):            #設一個遞迴
        global ans

        if row ==n :                           # 如果row已經等於N的話，代表已判斷完畢可將答案放入list中
            lst = []
            for i in col:
                s = ''
                for j in range(n):
                    if i == j:
                        s += 'Q'
                    else:
                        s += '-'
                lst.append(s)
            ans.append(lst)

        for i in range(n):                  # col list是放Q的攻擊範圍，如果檢查出來不再col裡，遞迴就可以結束,反之地迴會持續
            if (i not in col) and row - i not in r_sl and row + i not in l_sl:
                deep(n,row + 1,col+[i],r_sl+[row - i],l_sl+[row + i])      

    deep(N,0,[],[],[])                      #呼叫function


    return ans

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    