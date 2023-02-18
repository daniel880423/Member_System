def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    if N == 0: #若N=0,回傳空list
        return []
    ans = [] #建立一個空list存放結果
    def ABS(qs, sub_xy, sum_xy): #皇后位置,xy座標
        dump = len(qs)
        if dump == N:       #若放置的皇后數量=N，結果紀錄於list內,並結束遞迴
            ans.append(qs)
            return None
        for q in range(N):  #遞迴找布局
            if (q not in qs) and (dump-q not in sub_xy) and (dump+q not in sum_xy):
                ABS(qs+[q], sub_xy+[dump-q], sum_xy+[dump+q])

    ABS([], [], [])

    answer = [["-"*i + "Q" + "-"*(N-1-i) for i in j] for j in ans] #回傳答案
    return answer

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    