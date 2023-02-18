def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    
    dic = dict()

    def A  (size, price, visit, max_price):
        if (size, price) in dic:     #如果他已經存在過dic裡時
            return dic[(size, price)]  #return存的值
        if size <=  bag_size:
            max_price = price
        
        for i in range(len(items)):
            dic[(size, price)] = max_price   #建一個dic裡放 (size, price)=max_price
            if i not in visit and size <=  bag_size:
                max_price = max(A (size+items[i][0], price+items[i][1], visit+[i], max_price), max_price)
                #遞迴是一個max_price值 比較原本的跟新的 大的放進max_price
                
        return max_price


    ans = A(0, 0, [], 0)


    return ans

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    