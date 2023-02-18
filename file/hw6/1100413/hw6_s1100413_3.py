def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    len_nodes = len(nodes) #算題目的長度
    lst_sum = [] #把所有節點跟節點還有他們的距離的list放入此list
    for i in range(len_nodes-1): #跑nodes最外層的迴圈
        for j in range(len_nodes-1-i): #跑nodes的內層迴圈
            x = nodes[i][0] #nodes外層迴圈的曾迴圈的第一項
            y = nodes[i][1] #nodes外層迴圈的曾迴圈的第二項
            distance = abs(x-nodes[j+1+i][0])+abs(y-nodes[j+1+i][1])
            lst = [] #把第i個節點到其他節點的節點新增進來，也將他們之間的距離新增進來
            lst.append(distance) #把節點之間的距離新增進去list
            lst.append(i)
            lst.append(j+1+i)
            #print(lst)
            #print(distance)
            lst_sum.append(lst) #把新增好的list新增到他們的大集合list
    #print(lst_sum)
    new_lst_sum = sorted(lst_sum) #排序大list
    #print(new_lst_sum)
    len_new_lst_sum = len(new_lst_sum) #算大list的長度
    p = [] #代表某index節點的根結點
    for i in range(len_nodes):#初始化參數，代表某index節點的根結點
        p.append(i)
    #print(p)
     
    def find(idx): #更改跟節點
        if p[idx] != idx:
            p[idx] = find(p[idx])
        
        return p[idx]
    sum_distance = 0
    for i in range(len_new_lst_sum): #將nodes走訪一次就可以得出最小生成樹的最小距離，從距離小的開始走訪
        if find(new_lst_sum[i][1])!= find(new_lst_sum[i][2]):
            p[find(new_lst_sum[i][1])] = find(new_lst_sum[i][2])
            sum_distance +=new_lst_sum[i][0]

        else:
            continue
        

    return sum_distance #回傳所有最短路徑的和

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    