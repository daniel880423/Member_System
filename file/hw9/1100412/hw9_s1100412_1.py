def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    max_profit=0
    queue=[]
    for j in  range (len(items)):
        queue.append(items[j])
        queue[-1].append({j})
    total_visit=[]
    while  queue!=[]:
        total_visit = []
        for _ in range(len(queue)):
            x,y,z=queue.pop(0)
            for i in range (len(items)):    
                if z|{i} in total_visit or i in z:
                    continue
                size=x+items[i][0]
                if size>bag_size:
                    continue
                profit=y+items[i][1]
                if profit>max_profit:
                    max_profit=profit
                queue.append([size,profit,z|{i}])
                total_visit.append(z|{i})

    return max_profit



if __name__ == '__main__':
    bag_size = 4
    items =  [[2,95],[3,110],[4,50],[1,150],[2,120],[1,50]] 
    print(homework_9(bag_size, items))
    # 155

    