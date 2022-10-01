def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    c=1
    max=0
    ans=1
    l=len(nums)
    for i in range(l-1):   #跑0-長度-1,才符合所有元素
        if nums[i]==nums[i+1]:  #檢查是否等於下個
            c+=1   
            max=c          #斷點,儲存值
            if max>ans:    #比大小
                ans=max    #偌大於就替換值
        else:
            c=1       #不等於下個就重新累計
    return ans
if __name__ == '__main__':
    lst = [[50, 40, 100, -100, 40, 50]]
    print(homework_1(lst))
    