def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    if N== 0:
        return []
    result =[-1]*N
    row =0
    global a
    a=[]

    backtrack(result,row)
    return a

def backtrack(result,row):
    n=len(result)
    if row ==n:
        p=print_ans(result)
        a.append(p)
        return 
    for i in range(n):
        result[row]=i
        if isvalid(result,row):
            backtrack(result,row+1)    
    


def isvalid(ans,pos):
    valid =True
    for i in range(pos):
        diag= pos -i
        if ans[pos] in [ans[i],ans[i]-diag,ans[i]+diag]:
            valid =False
            break
    return valid

def print_ans(placed):
    #初始化p陣列為N*N
    p=['-'*len(placed)] * len(placed)
    for i ,Q in enumerate(placed):
        #第Q項顯示Q，其他維持-
        p[i]=p[i][:Q]+"Q"+p[i][Q+1:]
    return p 


if __name__ == '__main__':
    N =4
    print(homework_8(N))
    # [["Q"]]

