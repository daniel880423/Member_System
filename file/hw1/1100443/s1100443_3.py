def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    x=1
    max=0
    i=0
    len_nums=len(nums)
    for i in range(len_nums-1):
        if nums[i]==nums[i+1]:
            x+=1
        else:
            x=1
        if x>max:
            max=x
        

    return max

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    