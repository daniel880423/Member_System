def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    ans = queens(N)
    return output(ans,N)

def promising(state, nextX):    #判斷有無promising
    nextY = len(state)
    return any(abs(state[i] - nextX) in (0, nextY - i) for i in range(nextY))

def queens(n, state=()): #主函式
    if n==0:        
        return []
    if len(state) == n: 
        return [()]
    ans = []
    for pos in range(n):
        if not promising(state, pos):
            ans += [(pos,)+ result for result in queens(n, state + (pos,))]
    return ans

def output(ans,N): #印出答案
    record = []
    if N==1:
        return [["Q"]]
    for i in range(len(ans)):
        list = []
        for j in range(N):
            s = ""
            for k in range(N):
                if ans[i][j]==k:
                    s+="Q"
                else:
                    s+="-"
            list.append(s)
        record.append(list)
    return record

if __name__ == '__main__':
    N = 0
    print(homework_8(N))
    # [["Q"]]
    