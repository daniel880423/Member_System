def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search 

    #利用深度優先走訪
    def dfs(size,price,visit,max_price):
       if size <= bag_size :#判斷背包的重量超過總重量
           max_price = max(price,max_price)#比較出最大的price
       for i in range(len(items)):#依序比較每一項物品
           if size <= bag_size and i not in visit:#判斷背包的重量是否超過總重量與是否在visit裡面
               
               #比較出最大的price
               max_price = max(max_price,dfs(size+items[i][0],price+items[i][1],visit+[i],max_price))
       return max_price#回傳max price
    
    return dfs(0,0,[],0) #回傳結果
     



    

if __name__ == '__main__':
    bag_size = 12
    items =[[1, 108], [4, 129], [2, 113], [5, 62], [8, 194], [6, 61], [7, 51], [4, 110], [6, 198], [1, 194], [7, 85], [3, 87], [3, 129], [3, 117], [1, 112]]
    print(homework_9(bag_size, items))
    # 155
    