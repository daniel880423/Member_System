def homework_8(N):
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p==N:
            result.append(queens)
            return None
        for q in range(N):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
    result = []
    DFS([],[],[])
    if N==0:
        return []
    return [ ["-"*i + "Q" + "-"*(N-i-1) for i in sol] for sol in result]

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    