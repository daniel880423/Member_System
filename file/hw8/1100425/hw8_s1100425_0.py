def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    res = set()		# 存放每行的皇后放置的座標
    
    def find_pos(row, queen, N):
            for j in range(N):
                if pos_available(queen, (row, j)):
                    queen[row] = j
                    if row == N-1:    # 已經是最後一行並且找到了可以放的位置
                        res.add(tuple(queen))
                        return
                    else:   #沒到最後一行
                        find_pos(row+1, queen, N)
	# 檢驗當前位置是否可用
    def pos_available(queen, pos):
            # 放第i行  根據0~i-1行進行判斷
            for i in range(pos[0]):
                if queen[i] == pos[1]:  # 同列
                    return False
                elif abs(i-pos[0]) == abs(queen[i]-pos[1]): # 主副對角線
                    return False
            return True
	# 把座標形式打印成 Q...形式
    def plot_queen(queen, N):
            out = []
            for i in range(N):
                s = '.' * queen[i] + 'Q' * 1 + '.' * (N-queen[i]-1)
                out.append(s)
            return out

    # 初始皇后位置-1  
    queen = [-1 for _ in range(N)]  # 初始位置
        # 遞歸  從第0行開始
    find_pos(0, queen, N)
    out = []
    for t in res:
        out.append(plot_queen(t, N))
    return out   
   





     

if __name__ == '__main__':
    N = 7
    print(homework_8(N))
    # [["Q"]]
    