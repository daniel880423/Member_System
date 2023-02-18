
def DFS(queens, xy_dif, xy_sum, n):
    global result
    p = len(queens)
    if p==n:
        result.append(queens)
        return None
    for q in range(n):
        if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
            DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q], n)

def homework_8(N):
    global result
    result = []
    if N==0:
        return []
    DFS([],[],[],N)
    return [ ["-"*i + "Q" + "-"*(N-i-1) for i in sol] for sol in result]

if __name__ == '__main__':
    N = 9
    print(homework_8(N))




