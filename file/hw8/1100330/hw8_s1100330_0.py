def homework_8(N):
    if N == 0:
        N = 2
    result = []
    def DFS(queens, dif, sum):
        q = len(queens)
        if q < N:
            for i in range(N):
                if i not in queens and i-q not in dif and i+q not in sum: 
                    DFS(queens + [i], dif|{i-q}, sum|{i+q})  
        else:
            result.append(queens)
    
    DFS([], set(), set())
    return [[f'{"-"*i}Q{"-"*(N-i-1)}' for i in sol] for sol in result]

if __name__ == '__main__':
    N = 5
    print(homework_8(N))