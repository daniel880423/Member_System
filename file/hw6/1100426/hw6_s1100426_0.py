def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    P = []   #父節點
    l = []   #表示兩點距離
    l_total = 0
    number_of_line = 0
    
    ll = len(nodes)
    for i in range(ll):
        P.append(i)
        
    for i in range(ll):
        for j in range(ll):           
            length = abs(nodes[i][0]-nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])
            if i >= j:
                continue
            else:
                l.append([i, j, length])
    l = sorted(l, key=lambda x:x[2])
    
    
    print(l)
    def find(node) :
        if P[node] == node:
            return node

        else:
            return find(P[node])

             
        
        
        
        
        

    for i in range(len(l)):
        if find(l[i][0]) != find(l[i][1]):
            P[l[i][0]] = l[i][1]
            print(P)
            l_total += l[i][2]
            number_of_line+=1
            if number_of_line == ll-1:
                break
            




    return l_total

if __name__ == '__main__':
    nodes = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(homework_6(nodes))
    # 22
    