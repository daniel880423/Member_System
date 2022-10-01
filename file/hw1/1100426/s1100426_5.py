def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    max_num = 1  #最多連續數量
    l = len(nums)
    num = 1  #連續數量的統計
    for i in range(0, l-1):
        if nums[i] == nums[i+1]:
            num+=1
        else:
            num = 1
            continue
        if num > max_num:
            max_num = num
        
    return max_num

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    