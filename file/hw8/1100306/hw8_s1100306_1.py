def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    global ans
    ans = []
    result = [-1] * N
    row = 0
    backtrack(result, row)
    if N == 0:
        return []
    return ans
# def __init__(self):
#     self.ans = []
def backtrack(result, pos):
    n = len(result)
    if n == pos:
        board = []
        for i in result:
            row = ["-"] * n
            row[i] = "Q"
            board.append(''.join(row))
        ans.append(board)
        return
    for i in range(n):
        result[pos] = i
        if isvalid(result, pos):
            backtrack(result, pos+1)

def isvalid(result, pos):
    valid = True
    for i in range(pos):
        diag = pos - i
        if result[pos] in [result[i], result[i] - diag, result[i] + diag]:
            valid = False
            break

    return valid 

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    