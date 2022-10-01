def homework_1(nums):  # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    repeat_times = 1  # 重複次數
    max_repeat = 1  # 最大重複次數
    pre_element = None #上一個數字
    for i in nums:  # 跑一個大小為LST的迴圈
        if i == pre_element:  # 確認是否一致
            repeat_times += 1  # 重複次數+1
            max_repeat = max(repeat_times, max_repeat)  # 檢查重複次數與最大重複次數的大小
        else:  # 若不同
            pre_element = i
            repeat_times = 1  # 清空重複次數
    return max_repeat  # 回傳最大重複次數


if __name__ == '__main__':
    lst = [50, 40, 100, -100, 40, 50]
    print(homework_1(lst))
