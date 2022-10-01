def homework_1(nums):                           
    count_lst = []                              # 設一個儲存重複次數的List
    r = 0                                       # 令r為重複次數
    try:
        for i, num in enumerate(nums):
            r += 1
            if num != nums[i+1]:                # 與下一項不同
                count_lst.append(r)             # 不再重複所以存入次數
                r = 0                           # 歸零
    except IndexError:                          # 最後項無比較項直接加一
        count_lst.append(r)                     
        return max(count_lst)                   # 回傳重複次數的最大值

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    