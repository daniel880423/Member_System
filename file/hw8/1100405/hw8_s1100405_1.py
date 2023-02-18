def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    def DFS(Q, M, A):
        a = len(Q)

        if a == N:
            result.append(Q)
            return None

        for b in range(N):
            if b not in Q and a-b not in M and a+b not in A: 
                DFS(Q+[b], M+[a-b], A+[a+b])  

    result = []
    DFS([],[],[])
    
    ans = []
    c = 0
    for sol in result:
        ans.append([])
        print(sol)
        for i in sol:
            ans[c] += ["."*i + "Q" + "."*(N-i-1)]
        c += 1

    return ans

if __name__ == '__main__':
    N = 5
    print(homework_8(N))
    # [["Q"]]
    