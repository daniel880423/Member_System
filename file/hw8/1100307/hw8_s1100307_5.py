
def check(k,a,j):
    for i in range(k):
        if j == a[i] or abs(a[i]-j)==abs(i-k):
            return False
    return True
def homework_8(N): 
    global lst
    lst = []
    global a
    a = [-1]*N
    return path (0,N)
def path(k,n):
    global a
    global lst
    if k==n and len(a)!=0:
        ans = []
        for i in range(n):
            anss = ""
            for j in range(n):
                anss+="Q" if a[i] == j else "-"
            if len(anss)!=0:
                ans.append(anss)
        lst.append(ans)
    else:
        for j in range (n):
            if check(k,a,j):
                a[k] = j
                path(k+1,n)
    return(lst)



if __name__ == '__main__':
    N = 0
    print(homework_8(N))
    # [["Q"]]
     