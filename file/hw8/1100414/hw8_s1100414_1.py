def homework_8(N):
	if N==0:
		N=2
	sols = []
	def dfs(state, a, b): #設計『深度優先走訪』遞迴的函式
		r = len(state)
		if r < N: #使用a和b來儲存並檢查有沒有存在其他皇后
			for c in range(N):
				if c not in state and c-r not in a and c+r not in b:
					dfs(state+[c], a|{c-r}, b|{c+r})
		else: 
			sols.append(state) #如果最後長度 == n，那麼就成功分配好最後的棋盤分布
	
	dfs([], set(), set())
	return [[f'{"-"*p}Q{"-"*(N-p-1)}' for p in sol] for sol in sols] #最後再利用一維矩陣來表示 N x N 的棋盤格


if __name__ == '__main__':
    N = 0
    print(homework_8(N))
    # [["Q"]]