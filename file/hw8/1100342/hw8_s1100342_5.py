# def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
#     # depth first search + backtracking
#     if N== 0:
#         return []
#     solutions = []
#     stack = [[]]
#     count=0
#     while stack:
#         solution = stack.pop()
#         # if len(solution) > 1:
#         #     if  notSafe(solution[-1],solution[0:-1]):
#         #         continue
#         # if conflict(solution):
#         #     continue
#         row = len(solution)
#         if row == N:
#             solutions.append(solution)
#             count+=1
#             continue
#         for col in range(N-1,-1,-1):
#             queen = (row, col)
#             queens = solution.copy()
#             if len(solution) >= 1:
#                 if  notSafe(queen,queens):
#                     continue
#             queens.append(queen)

#             stack.append(queens)
    
#     p=[]
#     for i in solutions:
#         ans=[]
#         for j in range(N):         
#             ans.append(i[j][1])
#         p.append(print_ans(ans))
#     return count



# def conflict(queens):
#     for i in range(1, len(queens)):
#         for j in range(0, i):
#             a, b = queens[i]
#             c, d = queens[j]
#             if a == c or b == d or abs(a - c) == abs(b - d):
#                 return True
#     return False

# def print_ans(placed):
#     #初始化p陣列為N*N
#     p=['-'*len(placed)] * len(placed)
#     for i ,Q in enumerate(placed):
#         #第Q項顯示Q，其他維持-
#         p[i]=p[i][:Q]+"Q"+p[i][Q+1:]
#     return p  

# def notSafe(queen, queens):
#     return any(inCheck(queen, q) for q in queens)

# def inCheck(q1, q2):
#     return (q1[0] == q2[0] or # 同列
#             q1[1] == q2[1] or # 同行
#             abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])) # 對角線

# if __name__ == '__main__':
#     N =9
#     print(homework_8(N))
#     # [["Q"]]


def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking

    if N== 0:
        return []
    col=set()
    posDiag=set()#(r +c)
    negDiag= set()#(r-c)
    res= []
    # global count
    # count =0
    board =[["-"]*N for i in range(N)]
    def backtrack(r):
        # global count
        if r ==N:
            copy= ["".join(row)for row in board]
            res.append(copy)
            # count+=1
            return
        for c in range(N):
            if c in col or (r+c)in posDiag or (r-c)in negDiag:
                continue
            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c]="Q"
            backtrack(r +1)
            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r -c)
            board[r][c]="-"
    backtrack(0)
    return res

if __name__ == '__main__':
    N =9
    print(homework_8(N))
    #[["Q"]]

