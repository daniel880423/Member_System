def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    d_lst = []                                                 #創建list d_lst用來儲存[nodei,nodej,距離d]
    tree = []                                                  #創建list tree用來儲存node所連結的branch，預設值為自己
    w = 0                                                      #int w用來計算距離總和
    for i in range(len(nodes)):                                #利用for迴圈依序分析nodei
        tree.append(i)                                         #將nodes標號
        for j in range(i+1,len(nodes)):                        #利用for迴圈依序分析nodej
            d = c_dis(nodes[i],nodes[j])                       #利用建立的function計算nodei,nodej的距離d
            if d != 0:                                   
                d_lst.append([i,j,d])                          #將結果依 [nodei,nodej,d] 形式記錄在 d_lst
    d_lst.sort(key = lambda d_lst: d_lst[2])                   #依距離由小到大排序
   
    def find(x):                                               #建立遞迴函式find
        if x != tree[x]:                                       #如果index與儲存值不同             
            tree[x] = find(tree[x])                            #把儲存值當index再往下找
        return tree[x]                                         #回傳最後index與儲存值相同時的儲存值
    
    for i in range(len(d_lst)):                                #利用for迴圈由距離小到大檢查node的連結並記錄距離 
        if find(d_lst[i][0]) != find(d_lst[i][1]):             #若兩個node沒有連結在同一個樹上
            tree[find(d_lst[i][0])]  = find(tree[d_lst[i][1]]) #更新list tree將兩個點記錄在同一個樹上
            w += d_lst[i][2]                                   #紀錄距離
        else:                                                  #若兩個node已經連結在同一個樹上
            continue                                           #分析下一組
    return w                                                   #回傳最小生成樹距離總和

def c_dis(i,j):                                                #建立函式c_dis用來計算兩個node間的距離
        ans = abs(i[0]-j[0]) + abs(i[1]-j[1])                  #距離 = |xi - xj| + |yi - yj|
        return ans                                             #回傳距離值
                               
if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    