def homework_8(N):
	if N==0:
		N=2
	def DFS(s, xy_dif, xy_sum):
		p = len(s)
		if p==N:
			result.append(s)
			return None
		for q in range(N):
			if q not in s and p-q not in xy_dif and p+q not in xy_sum: 
				DFS(s+[q], xy_dif+[p-q], xy_sum+[p+q])  
	result = []
	DFS([],[],[])
	return [ ["-"*i + "Q" + "-"*(N-i-1) for i in sol] for sol in result]
if __name__ == '__main__':
    N = 8
    print(homework_8(N))
    # [["Q"]]