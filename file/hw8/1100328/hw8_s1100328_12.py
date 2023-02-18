def place(t): #找出是否在斜線位置
    for i in range(1, t):
        if t - i == abs(x[t] - x[i]):
           return False
    return True

def dfs(t):
    global ans
    if t > N:
        sol = [] #每一種答案
        for i in range(1, N + 1):
            temp = '' #每一行答案
            for j in range(1, N + 1):
                if j == x[i]: 
                  temp += 'Q'
                else: 
                  temp += '-'
            sol.append(temp)
        result.append(sol)
    else:
        for i in range(t, N + 1):
            x[t], x[i] = x[i], x[t] #透過交換 找出所有排列組合
            if place(t): dfs(t + 1) #如果可以place, dfs往下搜尋
            x[t], x[i] = x[i], x[t]

def homework_8(N):
  global x
  global result
  if N == 0:
    return []
  result = [] #所有答案
  x = [i for i in range(N + 1)]
  dfs(1)
  return result

if __name__ == '__main__':
  # 參考影片 https://www.youtube.com/watch?v=79mwcBrU8Lw
  N = 0
  print(homework_8(N))

































































"""
def DFS(queens, xy_dif, xy_sum, n):
    global result
    p = len(queens)
    if p==n:
        result.append(queens)
        return None
    for q in range(n):
        if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
            DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q], n)

def homework_8(N):
    global result
    result = []
    if N==0:
        return []
    DFS([],[],[],N)
    return [ ["-"*i + "Q" + "-"*(N-i-1) for i in sol] for sol in result]

if __name__ == '__main__':
    N = 9
    print(homework_8(N))
"""




