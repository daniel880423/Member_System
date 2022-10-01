def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    most_reapeat = 0
    count = 1
    pre_num = int()

    for i in nums:
        if i == pre_num:
            count = count + 1
            most_reapeat = max(count,most_reapeat)
        else:
            pre_num = i
            count = 1
            
    most_reapeat = max(count,most_reapeat)
    return most_reapeat
if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    