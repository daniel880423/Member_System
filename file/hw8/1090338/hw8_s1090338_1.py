def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
        res = set()		# 存放每行的皇后放置的座標

        def find_pos(row_index, queen, N): #遞歸
            for i in range(N):
                if pos_available(queen, (row_index, i)):
                    queen[row_index] = i
                    if row_index == N-1:    #已經是最後一行並且找到了可以放的位置
                        res.add(tuple(queen))
                        return
                    else:                   #沒到最後一行
                        find_pos(row_index+1, queen, N)
		
        def pos_available(queen, pos): #位置是否可用
            for i in range(pos[0]):     #放第i行 0~i-1行進行判斷
                if queen[i] == pos[1]:  #同列
                    return False
                elif abs(i-pos[0]) == abs(queen[i]-pos[1]): # 主副對角線
                    return False
            return True
		
        def plot_queen(queen, N): #印Ｑ位置圖
            out = []
            for i in range(N):
                s = '-' * queen[i] + 'Q' * 1 + '-' * (N-queen[i]-1)
                out.append(s)
            return out

        queen = [-1 for _ in range(N)]  # 初始位置
        find_pos(0, queen, N)   #遞歸 從第0行開始
        ans = []
        for t in res:
            ans.append(plot_queen(t, N))
        return ans

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    #[["Q"]]