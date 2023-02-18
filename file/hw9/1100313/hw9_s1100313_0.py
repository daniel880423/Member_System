def homework_9(bag_size, items):
    #此解題使用BFS
    total_visit=[]#走訪過的點
    max_price=0#最大價值
    length=len(items)
    for count in range(length):
        queue=[[items[count][0], items[count][1], {count}]] #佇列
        
        while queue!=[]:
            object=queue.pop(0)#把queue的第一個抓出來比較
            for i in range(length):
                v=set(list(object[2])+[i])#不同點的話則加上i，表示這兩點的組合
                
                #如果要比較的點是目前這個點，或是這兩點的組合已經比對過，或是重量超過最大背包重量，跳過它
                if i in object[2] or v in total_visit or object[0]+items[i][0]>bag_size:
                    continue
                size=object[0]+items[i][0]
                price=object[1]+items[i][1]
                total_visit.append(v)#把這兩點的組合新增到total_visit
                queue.append([size, price, v])#新增下一個queue
                max_price=max(price, max_price)#比較最大價值
            
    return max_price

if __name__ == '__main__':
    bag_size = 5
    items =  [[1,5],[3,1],[4,8],[6,100]]
    print(homework_9(bag_size, items))
    # 155
    