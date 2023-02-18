def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    global ans 
    ans = []
    if N == 0:
        return ans



    def deep(n,row,col,r_sl,l_sl):
        global ans

        if row ==n :
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



        for i in range(n):
            if (i not in col) and row - i not in r_sl and row + i not in l_sl:
                deep(n,row + 1,col+[i],r_sl+[row - i],l_sl+[row + i])      

    deep(N,0,[],[],[])




    return ans

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    