def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
#     global ans
#     ans = []
#     result = [-1] * N
#     row = 0
#     backtrack(result, row)
#     if N == 0:
#         return []
#     return ans

# def backtrack(result, pos):
#     n = len(result)
#     if n == pos:
#         board = []
#         for i in result:
#             row = ["-"] * n
#             row[i] = "Q"
#             board.append(''.join(row))
#         ans.append(board)
#         return
#     for i in range(n):
#         result[pos] = i
#         valid = True
#         for i in range(pos):
#             diag = pos - i
#             if result[pos] in [result[i], result[i] - diag, result[i] + diag]:
#                 valid = False
#                 break
#         if valid:
#             backtrack(result, pos+1)


# def isvalid(result, pos):
#     valid = True
#     for i in range(pos):
#         diag = pos - i
#         if result[pos] in [result[i], result[i] - diag, result[i] + diag]:
#             valid = False
#             break
#     return valid 

    # def DFS(queens, xy_dif, xy_sum):
    #     p = len(queens)
    #     if p==N:
    #         result.append(queens)
    #         return None
    #     for q in range(N):
    #         if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
    #             DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
    # result = []
    # DFS([],[],[])
    # if N == 0:
    #     return []
    # return [ ["-"*i + "Q" + "-"*(N-i-1) for i in sol] for sol in result]
    res = []
    cur = [['-'] * N for _ in range(N)]
    
    def backtracking(n, row, cur, res):
        if row == n:
            res.append([''.join(cur[i]) for i in range(n)])
            return 
        
        for j in range(n):
            if not is_valid(row, j, cur):
                continue
            cur[row][j] = 'Q'
            backtracking(n, row + 1, cur, res)
            cur[row][j] = '-'
    
    
    def is_valid(m, n, cur):
        for i in range(m):
            if cur[i][n] == 'Q':
                return False
            if n + m - i < len(cur) and cur[i][n + m - i] == 'Q':
                return False
            if n - m + i >= 0 and cur[i][n - m + i] == 'Q':
                return False
        
        return True
	
    backtracking(N, 0, cur, res)
    if N == 0:
        return []
    return res
if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    