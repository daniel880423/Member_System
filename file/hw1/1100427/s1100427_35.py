def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    n = []
    nums.append("")
    count = 1
    l = len(nums)
    for i in range(0, l-1):
        if nums[i] == nums[i+1]:
            count += 1
            
        
        else:
            n.append(count)
            count = 1
        
    ans = max(n)
    return ans

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    