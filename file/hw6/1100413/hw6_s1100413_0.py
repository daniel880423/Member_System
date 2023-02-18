def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    len_nodes = len(nodes)
    lst_sum = []
    for i in range(len_nodes-1):
        for j in range(len_nodes-1-i):
            x = nodes[i][0]
            y = nodes[i][1]
            distance = abs(x-nodes[j+1+i][0])+abs(y-nodes[j+1+i][1])
            lst = []
            lst.append(distance)
            lst.append(i)
            lst.append(j+1+i)
            #print(lst)
            #print(distance)
            lst_sum.append(lst)
    #print(lst_sum)
    new_lst_sum = sorted(lst_sum)
    #print(new_lst_sum)
    len_new_lst_sum = len(new_lst_sum)
    p = []
    for i in range(len_nodes):
        p.append(i)
    #print(p)
     
    def find(idx):
        if p[idx] != idx:
            p[idx] = find(p[idx])
        
        return p[idx]
    sum_distance = 0
    for i in range(len_new_lst_sum):
        if find(new_lst_sum[i][1])!= find(new_lst_sum[i][2]):
            p[find(new_lst_sum[i][1])] = find(new_lst_sum[i][2])
            sum_distance +=new_lst_sum[i][0]

        else:
            continue
        

    return sum_distance

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    