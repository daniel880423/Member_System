def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    def backtrack(i):
        if i == N and N!=0:
            bag.append(list(tree))
        for j in range(N):
            if j not in cols and j-i not in diag and j+i not in off_diag:  ##判斷是否同行與是否在主副對角線上
                cols.add(j)                         #加入第j行限制，為後面做準備
                diag.add(j-i)                       #加入主對角線限制，為後面做準備
                off_diag.add(j+i)                   #加入副對角線限制，為後面做準備
                tree.append("-"*(j)+"Q"+"-"*(N-j-1))    #將位置打印出來
                backtrack(i+1)                      #進入下一列判斷
                tree.pop()                          ##如果跑到這代表前面的會造成後面沒位置，有誤，刪除
                off_diag.remove(j+i)                #同上，刪除
                diag.remove(j-i)                    #同上，刪除
                cols.remove(j)                      #同上，刪除  
    bag = []
    tree = []
    cols = set()
    diag = set()
    off_diag = set()
    backtrack(0)
    return bag

if __name__ == '__main__':
    N = 9
    print(homework_8(N))
    # [["Q"]]

