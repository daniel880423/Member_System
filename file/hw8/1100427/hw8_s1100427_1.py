def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    a1 = []
    a2 = []
    if N == 0:
        return a2
    def to_sort(row, column, left_shift, right_shift, n, queen):
        if row >= n:
            a1.append(a2[:])
            return
        for i in range(n):
            if (i not in column) and (row+i not in left_shift) and (row-i not in right_shift):
                row_1 = ""
                for j  in range(n):
                    if j == i: row_1 += "Q"
                    else: row_1 += "-"
                a2.append(row_1)

                to_sort(row+1, column+[i], left_shift + [row+i], right_shift + [row-i], n, queen)
                a2.pop()

    to_sort(0, [], [], [], N, [])
    return a1

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    