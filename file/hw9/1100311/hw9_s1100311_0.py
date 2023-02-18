def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    l = len(items)
    dic = dict()     #設一個dict放每一次遞迴的最大值

    def deep(size,price,visit,max_p):
        if (size,price) in dic:           #檢查是否重複
            return dic[(size,price)]
        if size<= bag_size:                #更新max_price的值
            max_p = price
        for i in range(l):
            dic[(size,price)] = max_p      #把max_price放入dict中
            if i not in visit and size <= bag_size  :   #如果這個值每跑過和size還沒大於bag_size的時候，跑下一層遞迴
                
                max_p = max(deep(size+items[i][0],price +items[i][1], visit +[i],max_p),max_p) #下一個max_price跟前一個比大小
                

                
        return max_p #輸出最大值

    ans = deep(0,0,[],0)

    return ans

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    