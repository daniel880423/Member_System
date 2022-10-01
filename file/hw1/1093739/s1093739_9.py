def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    max_times = 0 #假設最多次
    original_times = 1 #原本的次數
    original_element = None #前一個數字
    count_times = [1] #將次數放入此list
 
    for i in nums:
        if i == original_element:#判斷下一個數字是否等於前一個數字
            original_times += 1
            max_times = original_times
            count_times.append(max_times)#將每個數字的連續次數放入
        else:
            original_element = i
            original_times = 1
        max_times = max(count_times)#計算出連續次數的最大值並回傳
            
            

    return (max_times)

if __name__ == '__main__':
    lst = [10, 11, 54, 54, 21, 61, 61, 61, 12, 1000, 100, 1000, 1000, 1000, 1000, 999, 999, 999 ]
    print(homework_1(lst))
    