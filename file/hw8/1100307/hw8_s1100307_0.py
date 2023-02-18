def draw(a):
    ans = []
    for i in range(len(a)):
        anss = ""
        for i in range(a[i]):
            anss+="-"
        anss+='Q'
        for h in range(len(a)-len(anss)):
            anss+="-"
        ans.append(anss)
    return ans
def check(a,n):
    l = len(a)
    if l == 0:
        return True
    for i in range(l):
        if n == a[i]:
            return False
        elif abs(n-a[i])==abs(l-i):
            return False
    return True
def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)# depth first search + backtracking
    
    ans = []
    for jj in range(N):
        a = [jj]
        for i in range (N):
            for j in range(N):
                if check(a,j):
                    a.append(j)
                    break
                else:
                    continue
            if len(a)==N:
                ans.append(draw(a))
                a= []
    return ans


        

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    