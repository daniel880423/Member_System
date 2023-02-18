def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    Max_price=0
    q=[]
    v=set()
    for i in range(len(items)):
        if items[i][0]>bag_size or tuple(items[i]) in v:
            continue
        q.append(items[i] + [{i}])
        v.add(tuple(items[i]))

    while q:
        tv=[]
        for j in range(len(q)):
            a=q.pop(0)
            a0=a[0]
            a1=a[1]
            a2=a[2]        
            if a0 <= bag_size:
                Max_price=max(a1,Max_price)
            if a0 == bag_size:
                continue
            for i in range(len(items)):
                b=a0+items[i][0]
                c=a1+items[i][1]
                d=a2 | {i}
                if i not in a2 and b<=bag_size and d not in tv:
                    q.append([b,c,d])
                    tv.append
                        
    return Max_price
    # q = [[1,25,{0}],[4,120],[4,30],[1,130],[2,20]]
if __name__ == '__main__':
    bag_size = 12
    items = [[1, 108], [4, 129], [2, 113], [5, 62], [8, 194], [6, 61], [7, 51], [4, 110], [6, 198], [1, 194], [7, 85], [3, 87], [3, 129], [3, 117], [1, 112]]
    print(homework_9(bag_size, items))
    # 155
    