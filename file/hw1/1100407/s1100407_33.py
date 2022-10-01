def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    ans = 0
    count = 0
    x = 0
    for n in nums:
        if n == x:
            count+=1
        else:
            x = n
            count = 1
        if ans < count:
            ans = count
    return ans

if __name__ == '__main__':
    lst = [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]
    print(homework_1(lst))
    