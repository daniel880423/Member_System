def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count=1
    i=0
    max=0
    lenlist=len(nums)
    for i in range (lenlist-1):
        if nums[i] == nums[i+1]:
            count += 1
        else:
            count = 1
        if count > max:
            max=count



    return max

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    