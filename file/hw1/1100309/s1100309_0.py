def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count = 1
    ans = 1
    numbers = len(nums) - 1          #先算出list有幾個字                         
    for i in range(numbers):         
        if nums[i] == nums[i+1]:     #如果前後數字一樣
            count += 1               #count 加1
            if count > ans:          #如果count大於1，ans就變成count
                ans = count
        else:
            count =  1               #如果前後數字不一樣，count變回1，從頭算
            
    if count > ans:                  #如果有另一個count大於上一個，就取代為答案
        ans = count
    

    return ans                       #回傳答案

if __name__ == '__main__':
          
    lst = [10,11,54,54,21,61,61,61,12]
    print(homework_1(lst))
    