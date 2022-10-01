def homework_1(nums): 
    max_time=1      #最大出現次數 
    time=0          #出現幾次
    pre=None        #記錄上一個元素
    for i in nums:
        if i==pre:  #跟上一個元素一樣
            time+=1 #出現次數+1
            if time>max_time:   #假如出現次數大於最大出現次數
                max_time=time   #改掉最大出現次
        else:       
            pre=i   #更新上一個元素
            time=1  #出現次數更新成1
    return max_time

if __name__ == '__main__':
    lst =  [50, 40, 100, -100, 40, 50]
    print(homework_1(lst))
    