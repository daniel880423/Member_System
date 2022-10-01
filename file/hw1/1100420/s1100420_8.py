def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    number=1 
    max=0
    i=1
    len_nums=len(nums)
    for i in range(len_nums-1):
        if nums[i] == nums[i+1]:
            number+=1
        else:
            number=1
        if number>max:
            max=number

    return max

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    