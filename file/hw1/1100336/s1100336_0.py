def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
#用字典試試
    count=1   #設一個count來累計重複幾次
    max_count=0   #設一個變數來存重複最多次的數字的次數
    for i in range(len(nums)-1):  #把lst中的每個數和下一個數比較
        if  nums[i]==nums[i+1]:   #如果等於下一個數
            count+=1              #count加一
            if count>=max_count:  #如果count>重複最多次的數字的次數
                max_count=count  #把重複最多次的數字的次數設為count
        else :       #如果不等於下一個數
            count=1  #把count重設為一
                
            


    return max_count

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    #lst= [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]
    #lst= [10,11,54,54,21,61,61,61,12]
    print(homework_1(lst))
