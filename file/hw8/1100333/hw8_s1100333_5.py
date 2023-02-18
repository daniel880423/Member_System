 # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
def homework_8(N: int) -> List[List[str]]:
    def is_valid(queens, row, col):
        for queen in queens:
            if queen[1] == col:
                return False
        for queen in queens:
            row_distance = abs(queen[0] - row)
            col_distance = abs(queen[1] - col)
            if row_distance == col_distance:
                return False
        return True

    def dfs(queens, row):
        if row == N:
            result.append(queens)
            return
        for col in range(N):
            if is_valid(queens, row, col):
                dfs(queens + [(row, col)], row + 1)

    result = []
    dfs([], 0)
    return [["-" if (row, col) not in sol else "Q" for col in range(N)] for sol in result for row in range(N)]