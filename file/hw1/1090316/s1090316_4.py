def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    max_time = 1   # 已知最大連續出現次數初始為0
    cur_time = 1   # 紀錄當前元素是第幾次連續出現
    pre_element = None   # 紀錄上一個元素是什麼

    for i in nums:
        if i == pre_element:   # 如果當前元素和上一個元素相同,連續出現次數+1,並更新最大值
            cur_time += 1
            max_time = max((cur_time, max_time))
        else:   # 不同則刷新計數器
            pre_element = i
            cur_time = 1


    return max_time

if __name__ == '__main__':
    lst = [3,3 ,3,2,2,3]
    print(homework_1(lst))
    