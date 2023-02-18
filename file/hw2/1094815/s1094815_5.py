def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    Max = 0
    Times = 1
    for i in range(len(nums)-1):
        Times += 1
        if Times > Max:
            Max = Times
        if nums[i] != nums[i+1]:
            Times = 1

    return Max
    