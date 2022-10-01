def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    max_t = 1 #最大連續出現
    now_t = 1 #現在連續出現
    pre_num = None
    for i in nums:
        if i == pre_num:
            now_t +=1
            max_t = max(max_t,now_t)
        else:
            pre_num = i
            now_t = 1
    return max_t

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    