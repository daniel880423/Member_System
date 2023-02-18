def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    global max_price

    def DFS(size, price, visit, max_price):
        if size <= bag_size:
            max_price = price
            
        if (size, price) not in dic_visit:
                dic_visit[(size, price)] = max_price
        else:
            return dic_visit[(size, price)] 

        for j in range(len_items):
            if j not in visit:
                if size <= bag_size:
                    max_price = max(DFS(size+items[j][0], price+items[j][1], visit+[j], max_price), max_price)  
               
        return max_price


    dic_visit = {}
    len_items = len(items)                    
    ans = DFS(0, 0, [], 0)
    return ans



if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    