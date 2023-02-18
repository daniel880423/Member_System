def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    

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
        if (col == N):
            ans = []
            a=""
            for i in range(N):
                for j in range(N):
                    a+=array[i][j]
                ans.append(a)
                a=""
            total.append(ans)
            return True

        res = False
        for i in range(N):
            if (promising(array, i, col)):
                array[i][col] = "Q"
                res = queen(array, col + 1) or res
                array[i][col] = "-"  
 
        return res

    total = []
    array = []
    for i in range (0, N):
        array.append(["-"]*N)
    if queen(array, 0) == False or total == [[]]:
        return []
    else:
        total.sort()
        return total

if __name__ == '__main__':
    N = 0
    print(homework_8(N))
    # [["Q"]]
    