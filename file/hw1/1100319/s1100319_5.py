def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    time = 1                #次數
    max = 0                 #最大次數
    pre_num = None          #前一個數
    
    for i in nums:
        if i == pre_num:    #每取到一個數就將其與前一個數比較，若相同
            time +=1        #次數+1
            if max < time:  
                max = time
        else:               #若不同
            pre_num = i     #將前一個的數取代成目前的數
            time = 1        #次數重設為1
    
    if max == 0:            #全部數字皆不重複
        max = 1        
    
    return max

if __name__ == '__main__':
    lst =  [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    