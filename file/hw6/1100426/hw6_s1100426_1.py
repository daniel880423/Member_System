def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    P = []   #父節點
    l = []   #表示兩點距離
    l_total = 0  #總長度
    number_of_line = 0 #連線數目
    
    ll = len(nodes)
    for i in range(ll):
        P.append(i)
        
    for i in range(ll):
        for j in range(ll):           #算長度
            length = abs(nodes[i][0]-nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])
            if i >= j:   
                continue
            else:
                l.append([i, j, length])
    l = sorted(l, key=lambda x:x[2])   #以長度做排序
    
    
    # print(l)
    def find(node) :   #找根節點
        if P[node] == node:
            return node
        else:
            return find(P[node])
        # if P[node] != node:
        #     P[node] = find(P[node])
        # return P[node]

             
        
        
        
        
        

    for i in range(len(l)):   
        if find(l[i][0]) != find(l[i][1]):  #若根節點不同，即將根節點相連
            # P[l[i][0]] = l[i][1]
            P[find(l[i][0])] = find(l[i][1])
            # print(P)
            l_total += l[i][2]
            number_of_line+=1
            if number_of_line == ll-1: #若(節點-1)=線的數量，就跳出迴圈
                break
            




    return l_total

if __name__ == '__main__':
    nodes = [[5, 0], [-1, 4], [1, 7], [7, -1], [2, 1], [3, -9]]
    print(homework_6(nodes))
    # 22
    