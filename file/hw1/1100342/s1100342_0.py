def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    length = len(nums)#計算長度
    con =[]#連續次數
    count = 0#累計個數
    for i in range(1,length):
        if nums[i-1] != nums[i]:
            n=i-count
            con.append(n)
            count +=n 
    last = length-count
    con.append(last)
    ans = max(con)#找最大連續次數
            
    return ans

if __name__ == '__main__':
    lst =  [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]


    print(homework_1(lst))
    