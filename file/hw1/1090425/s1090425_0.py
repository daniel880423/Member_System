def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count_lst = []
    r = 0
    try:
        for i, num in enumerate(nums):
            if num == nums[i+1]:
                r += 1
            else:
                r += 1
                count_lst.append(r)
                r = 0
    except IndexError:
        r += 1
        count_lst.append(r)
        return max(count_lst)

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    