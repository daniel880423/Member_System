def homework_1(nums): 
    max = 0                     #存目前連續出現最多的次數
    tmp = 0                     #存lst中上一個數字
    count = 1                   #數連續出現了幾次
    for i in nums:              
        if i == tmp:            #如果跟上個一樣count加1
            count += 1
        else:                   #不同就判斷一下是否超過之前的次數然後重新開始數
            if max < count:
                max = count
            tmp = i
            count = 1
            continue
    if max < count:             #判斷最後一個是否有超過之前的
                max = count
    return max         

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    