def homework_1(nums):   
    a = 1                   #記錄初始最大連續次數
    sum = 1                 #記錄元素第幾次出現
    pre = None              #記錄上一個元素
    c = len(nums)           #計算列表中有機個元素
    for i in range (c) :    
        if nums[i] == pre:  #列表中的元素等於上一個元素
            sum += 1        #如果等於上一個元素就+1，因為第一次出現的元素一定不會等於前一個，所以sum = 1
            pre = nums[i]   #將現在的元素定義成上一個出現的元素再進入下個迴圈
            if sum > a:
                a = sum     #利用比大小求出連續出現最多的個數
        else:               #列表中的元素不等於上一個元素
            sum = 1         #重新定義元素第幾次出現
            pre = nums[i]   #將現在的元素定義成上一個出現的元素再進入下個迴圈
    return a                #a為最大的元素連續次數
if __name__ == '__main__':
    lst = [10,11,54,54,21,61,61,61,12]
    print(homework_1(lst))