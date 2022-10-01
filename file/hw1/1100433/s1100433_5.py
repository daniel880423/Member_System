def homework_1(nums):              # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    streak = 0
    c = 1
    a = 0
    for i in nums:
        if i == a:
            c += 1
        else:
            c = 1
            a = i
        if c > streak:
            streak = c
    return streak

if __name__ == '__main__':
    lst = [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]
    print(homework_1(lst))
    