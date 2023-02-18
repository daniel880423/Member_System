def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    def ABS(queens,xy_sub,xy_sum):                       #以遞回函式檢查皇后xy座標有無其他皇后
        count=len(queens)
        if count==N:                                     #若放置的皇后數量為N，加到list
            ans.append(queens)
            return None
        for qun in range(N):                             #尋找可放皇后的位置是否與當前的皇后位置相鄰（包括上下，左右）或同一對角線上
            if qun not in queens and count-qun not in xy_sub and count+qun not in xy_sum: 
                ABS(queens+[qun],xy_sub+[count-qun],xy_sum+[count+qun])

    
    ans=[]
    ABS([],[],[])
    if N == 0:
            return []
    return [["-" * i + "Q" + "-" * (N-i-1) for i in sol] for sol in ans]

    

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    