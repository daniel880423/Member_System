def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking

    frame= (queen(N,()))                                                #將得到的排法指定給frame
    board = []                                                          #建立空list以儲存排法
    for i in frame:                                                     #選出其中一種排法
        ans = []                                                        #建立空list以儲存排法
        for j in i:                                                     #找出每一列皇后擺放的位置
            queens=""
            for k in range(N):                                          
                if j !=k:                                               #當還沒到此列皇后擺放位置時，印出"-"
                    queens += "-"
                else:                                                   #到了之後，印出"Q"
                    queens += "Q"
            ans.append(queens)                                          #將此列結果append到此擺法的ans
        board.append(ans)                                               #找到此擺法的完整擺法
    return board        
def conflict(state,nextX):
    nextY = len(state)
    if any(abs(state[i]-nextX)==0 for i in range(len(state))):          #如果有任何皇后同行 回傳True
        return True
    if any(abs(state[i]-nextX)== nextY-i for i in range(len(state))):   #如果有任何皇后同對角線 回傳True
        return True
    return False
def queen (n,state):
    if len(state) == n:                                                 #當皇后已經擺上去N個了 回傳得到的排列方式
        return[()]
    ans = []
    for pos in range(n):
        if not conflict(state,pos):                                     #只要沒有任何皇后同行同對角線，在最新的一列中放入得到的位置
            ans += [(pos,)+ result for result in queen(n,state+(pos,))]
    return ans
if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    