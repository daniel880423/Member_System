def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)  
    current_time = 1  
    most_time = 1    #累積最高次數
    pre_element = None  #上一個數字，一開始設為空

    for i in nums:
        if i == pre_element:   #測驗上一個元素跟目前元素是否相同
            current_time += 1  #如果相同則加一
            most_time = max(most_time,current_time) #紀錄最高次數

        else:
            pre_element = i  #與上一個元素不同則重新計算
            current_time = 1   
        
    return most_time

if __name__ == '__main__':
    lst = [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]

    print(homework_1(lst))