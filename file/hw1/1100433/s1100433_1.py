def homework_1(nums):              # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    c = 1
    streak = 0
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            c += 1
        else:
            c = 1
        if c > streak:
            streak = c
    return streak

if __name__ == '__main__':
    lst = [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]
    print(homework_1(lst))
    