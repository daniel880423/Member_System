def homework_1(nums):               # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    times = 1
    ans = 1
    numbers = len(nums) - 1          #先算出list有幾個字                         
    for i in range(numbers):         
        if nums[i+1] == nums[i]:     #如果前後數字一樣
            times += 1               #times 加1
            if times > ans:          #如果times大於1，ans就變成times
                ans = times
        else:
            times =  1               #如果前後數字不一樣，times變回1，從頭算
            
    if times > ans:                  #如果有另一個times大於上一個，就取代為答案
        ans = times
    

    return ans                       #回傳答案

if __name__ == '__main__':
          
    lst = [10,11,54,54,21,61,61,61,12]
    print(homework_1(lst))
    