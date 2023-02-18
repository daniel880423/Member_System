def homework_8(N):# 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    answer = []
    answer_2 = []


    if N == 0:
        return answer_2
    

    def to_sort_chess(row , column, shift_left, shift_right, n, queen):
        if row >= n:
            answer.append(answer_2[:])
            return
        
        for i in range(n):

            if (i not in column) and (row + i not in shift_left) and (row - i not in shift_right) :
                roww = ""
                for j in range(n):
                    if j == i: roww += "Q"
                    else: roww += "-"
                answer_2.append(roww)


                to_sort_chess(row+1, column + [i], shift_left + [row+i], shift_right + [row-i], n, queen)
                answer_2.pop()
    to_sort_chess(0, [], [], [], N, [])
    return answer

if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    