def check(k,z,j):
    for i in range(k):
        if j == z[i]:
            return False
        elif abs(z[i]-j)==abs(i-k):
            return False
    return True

def draw(z,n):
    ans = []
    for i in range(n):
        anss = ""
        for j in range(z[i]):
            anss+="-"
        anss+='Q'
        for h in range(n-len(anss)):
            anss+="-"
        ans.append(anss)
    return ans

def homework_8(N): 
    global lst
    lst = []
    global z
    z = [-1]*N
    return path (0,N)
    
def path(k,n):
    global z
    global lst
    if k==n:
        lst.append(draw(z,n))
    else:
        for j in range (N):
            if check(k,z,j):
                z[k] = j
                path(k+1,n)
    return(lst)



if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
     