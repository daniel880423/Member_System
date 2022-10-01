def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    c=1
    max=0
    i=0
    _len=len(nums)
    for i in range(_len-1):
        if nums[i]==nums[i+1]:
            c+=1
        else:
            c=1
        if c>max:
            max=c
    return max

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    