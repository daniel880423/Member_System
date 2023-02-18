def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    array = []
    for i in range (0, N):
        array.append(["-"]*N)

    def promising(array, row, col):
    # Check this row on left side
        for i in range(col):
            if array[row][i] == "Q":
                return False
 
    # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if array[i][j] == "Q":
                return False
 
    # Check lower diagonal on left side
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if array[i][j] == "Q":
                return False

        return True
    
    def queen(array, col):
        if col >= N:
            return True
        for i in range(N):
            if promising(array, i, col):
                array[i][col] = "Q"

                if queen(array, col + 1) == True:
                   return True

                array[i][col] = "-"

    queen(array, 0)
    ans = []
    a = []
    for i in range(N):
        for j in range(N):
            a+=array[i][j]
        ans.append(a)
        a=[]
    return ans

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    