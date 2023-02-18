def homework_8(N):
    def dfs(queens, xy_dif, xy_sum):
        q = len(queens)
        if q==N:
            result.append(queens)
            return None
        for i in range(N):
            if i not in queens and q-i not in xy_dif and q+i not in xy_sum: 
                dfs(queens+[i], xy_dif+[q-i], xy_sum+[q+i])  
    result = []
    dfs([],[],[])
    return [ ["."*i + "Q" + "."*(N-i-1) for i in sol] for sol in result]

if __name__ == '__main__':
    N = 5
    print(homework_8(N))