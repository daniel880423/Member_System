def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    global ans 
    ans = []
    if N == 0:
        return ans
    
    def queen(N, row, col, rs, ls):
        global ans
        if (row == N):
            lst = []
            for i in col:
                a = ''
                for j in range(N):
                    if i == j:
                        a += "Q"
                    else:
                        a += "-"
                lst.append(a)
            ans.append(lst)
            return

        for i in range(N):
            if (i not in col) and (row-i not in rs) and (row+i not in ls):
                queen(N, row+1, col+[i], rs+[row-i], ls+[row+i])



    queen(N, 0, [], [], [])

    return ans

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    