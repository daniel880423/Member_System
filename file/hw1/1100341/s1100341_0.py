def homework_1(nums): 
    time = 0           #time=連續次數最多的數字的次數
    last = 0           #lst中的上一個數字
    c = 1              #連續的次數
    for i in nums:
        if i == last:  #數字跟上一個數字一樣次數就加1
            c += 1
        else:
            if c > time:     #如果計算中的連續次數>原本的次數時
                time = c     #time的值就變成新的c
            last = i         
            c = 1
            continue
    if c > time:       #檢查最後的time值是否是最大的
        time = c
    return time
   
    
   

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    print(len(lst))
    if len(lst) < 3:          #len長度要在3~1000之間 否則就print error
        print("error")
    elif len(lst) > 1000:
        print("error")

    