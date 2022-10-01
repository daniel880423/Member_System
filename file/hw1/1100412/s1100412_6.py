def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    appear_times = 0                                #設pre_number的出現次數為0
    max_times = 0                                   #設連續出現的最多次數為0
    pre_number=nums[0]                              #設nums中的第一個數為pre_number
    for i in nums:                                  #for迴圈，從第一個數字開始找
        if(i == pre_number ):                       
            appear_times += 1                       #如果與前一個數字相同，pre_number的連續出現次數+1
            max_times = max(appear_times,max_times) #如果出現更大的最大連續次數，將max_times設為此次數
        else:
            appear_times = 1                        #出現不同的數字時，為此數字重新設定appear_times = 1 
            pre_number = i                          #將新的數字設為pre_number


    return max_times                                #回傳出現的最大連續次數



if __name__ == '__main__':
    lst = [10,11,54,54,21,61,61,61,12]
    print(homework_1(lst))
    