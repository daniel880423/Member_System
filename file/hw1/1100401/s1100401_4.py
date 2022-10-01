from operator import length_hint


def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    ans = 0
    i = 0
    count = 1
    lens = len(nums)
    while True:
        while nums[i] == nums[i+1]:
            count+=1
            i+=1
            if i+1 == lens:
                break
        if count > ans:
            ans = count
        count = 1 
        i+=1
        if i >= lens or ans >= lens-i:
            break
    return ans
    

if __name__ == '__main__':
    lst =  [10, 11, 54, 54, 21, 61, 61, 61, 12]
    print(homework_1(lst))
    