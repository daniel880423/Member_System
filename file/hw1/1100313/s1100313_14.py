def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count = 1                        #設定第一個元素的次數為1
    maximum = 0                      #連續出現最多次的次數
    length = len(nums)
    for i in range(length-1):        #從第二個元素開始計算              

        if nums[i+1] == nums[i]:     #若現在的元素跟前一個元素一樣
            count+=1                 #計數+1
        else:                        #不同則計數重新計算
            count = 1
            
        if count > maximum:          #如果出現次數大於原本的最多次數
            maximum = count          #替代
    
    return maximum                   #return出現連續最多的次數

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    