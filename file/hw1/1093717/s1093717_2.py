def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    max_time = 1
    current_time = 1
    last_item = None
    for i in nums:
        if i == last_item:
            current_time += 1
            max_time = max((current_time,max_time))
        else:
            last_item = i
            current_time = 1

    return max_time

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    