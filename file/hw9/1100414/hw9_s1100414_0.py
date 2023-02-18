def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    n=len(items)
    w=[]
    v=[]
    for i in range(n):
        w.append(items[i][0])
    for i in range(n):
        v.append(items[i][1])
    global bestV,curW,curV,x,bestx
    x=[False for i in range(n)]
    bestV=0
    curW=0
    curV=0
    bestx=None
    def backtrack(i):
        global bestV,curW,curV,x,bestx
        if i>=n:
            if bestV<curV:
                bestV=curV
                bestx=x[:]
        else:
            if curW+w[i]<=bag_size:
                x[i]=True
                curW +=w[i]
                curV +=v[i]
                backtrack(i+1)
                curW-=w[i]
                curV-=v[i]
            x[i]=False
            backtrack(i+ 1)

    backtrack(0)
    return bestV


if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
   
    