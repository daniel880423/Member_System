def homework_1(nums):  # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    next_element = nums[1]  # 下一個數字
    repeat_times = 1  # 重複次數
    max_repeat = 0  # 最大重複次數
    for i in nums:  # 跑一個大小為LST的迴圈
        if i == next_element:  # 若lst[0] == lst[1]
            repeat_times += 1  # 重複次數+1
            max_repeat = max(repeat_times, max_repeat)  # 檢查重複次數與最大重複次數的大小
        else:  # 若不同
            next_element = i  # 前一個數字為目前i的數字
            repeat_times = 1  # 清空重複次數
            max_repeat = max(repeat_times, max_repeat)
    return max_repeat  # 回傳最大重複次數


if __name__ == '__main__':
    lst = [50, 40, 100, -100, 40, 50]
    print(homework_1(lst))
