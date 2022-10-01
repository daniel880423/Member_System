# from asyncio.windows_events import NULL


def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    ans_list = [0] # 內容是放出現不同數字出現的 索引位置
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:# 當前後數字不同
            ans_list.append(i)  # 將後面數字的索引位置添加到ans_list中
    ans_list.append(len(nums))# 將nums的總長度添加到ans_list中
    ans = 0 # 用來放答案
    for j in range(1,len(ans_list)):
        ans = max(ans, ans_list[j]-ans_list[j-1])# 比較ans 跟 前後索引位置的差值(即為一段相同數字的長度) 誰比較大
    return ans # 得出最長的相同數字長度,並回傳

if __name__ == '__main__':
    lst =   [1,1,1,1,1,1,1,1,1]

    print(homework_1(lst))
    