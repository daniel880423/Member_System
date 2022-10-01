def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    length = len(nums)#計算長度
    count = 0#累計個數
    ans=0#最大連續次數
    for i in range(1,length):
        if nums[i-1] != nums[i]:
            n=i-count
            count +=n
            if n >ans:
                ans = n 
    last = length-count
    if last>ans:
        ans = last

            
    return ans

if __name__ == '__main__':
    lst =   [0,0,1,1,1,1,0,0,0,1]


    print(homework_1(lst))
    