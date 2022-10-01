def homework_1(nums):# 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(nums)>1000 or len(nums)<3 :
        return "False"
    for i in nums:
        if type(i) is not int or abs(i) > 10000:
            return "False"
    count = 1
    list=[]
    for k in range(1,len(nums)):
        if nums[k]==nums[k-1]:
            count += 1
            list.append(count)
        else:
            count=0
            list.append(count)
    R=max(list)+1
    if len(set(nums)) == 1:
        R=len(nums)
        
    return R

if __name__ == '__main__':
    lst = [-11, -11, -11, -11, -11, -11, -11, -11, -11, -11, -11, -11, -11, -11, -11, -11, -11, -11]
    print(homework_1(lst))