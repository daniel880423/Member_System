def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    lst = []
    lst_num = 0
    
    homework_8.col = ["" * N for i in range(N)]
    
    for i in range(N):
        homework_8.col[0] = i 
        queens(0)
    
    
    
    
    
    
    
    ans = ["-" * N for i in range(N)]



    lst.insert(lst_num, ans)
    lst_num += 1


    return homework_8.col

def queens(x):
    if promising(x):
        if x == N - 1:

            return 
        else:
            for j in range(N):
                homework_8.col[x + 1] = j
                
                if not queens(x + 1) and homework_8.col[x + 1] == N - 1:
                    homework_8.col[x + 1] = ""

def promising(x):
    k = 0
    switch = True
    while(k < x and switch):
        if homework_8.col[x] == homework_8.col[k] or abs(homework_8.col[x] - homework_8.col[k] == x - k):
            switch = False
        k += 1
    
    return switch

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    