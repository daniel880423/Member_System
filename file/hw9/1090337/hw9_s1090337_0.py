def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    max=[0] #答案紀錄(最大值)
    n=len(items)  #items總數
    def go(s,p,po,v,c):#s:size  p:累加值 po:前一累加值 v:已使用紀錄 c:已相加次數
        if s==bag_size or c==n: #相加後剛好到最大 or 相加後未滿
            if p>max[0]:
                max[0]=p
            return
        if s>bag_size: #相加後超過
            if po>max[0]:#扣掉最後累加的值後比較
                max[0]=po
            return
        for i in range(n): #靠迴圈相加
            if (i not in v): 
                #print(s)
                #print(p)
                
                go(s+items[i][0],p+items[i][1],p,v+[i],c+1)  #遞迴
                #[{0},{0,1},{0,1,2},{1},{1,2}]

        
    go(0,0,0,[],0)

    return max[0]

if __name__ == '__main__':
    bag_size = 25
    items = [[1, 108], [4, 129], [2, 113], [5, 62], [8, 194], [6, 61], [7, 51], [4, 110], [6, 198], [1, 194], [7, 85], [3, 87], [3, 129], [3, 117], [1, 112]]
    print(homework_9(bag_size, items))
    # 155
    