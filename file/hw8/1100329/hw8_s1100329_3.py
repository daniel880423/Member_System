def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    def promising(i,j,tree):                                ##設立判斷function
        for k in range(i):
            if (tree[k]==j) or abs(tree[k]-j) == abs(k - i): ##如果同行列或斜線就回傳false
                return False
        return True     
                    
    def queens(i,j,tree,bag):
        for k in range(N):
            if promising(i,k,tree):       ##進入判斷function
                tree[i] = k               #如果function回傳true，代表該位置可放皇后
                if i == N-1 :             #如果跑到最後，去將答案打印出來
                    t=[]
                    for p in range(N):
                        row= '-' * tree[p] + 'Q' * 1 + '-' * (N-tree[p]-1) ##輸出字串
                        t.append(row)
                    bag.append(t)
                else:                     #i+1，從頭遞迴
                    queens(i+1,N,tree,bag)
        return bag
    bag=[]
    A=N*[0]
    return queens(0,N,A,bag)

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]

