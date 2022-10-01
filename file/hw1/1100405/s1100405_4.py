def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    out_lst = []
    a = nums[0]
    out = 0

    for i in nums:
        if i != a:
            a = i
            out_lst += [out]
            out = 1
        else:
            out += 1
    out_lst += [out]
    out_lst.sort()

    return out_lst[-1]

if __name__ == '__main__':
    lst = [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]
    print(homework_1(lst))
    