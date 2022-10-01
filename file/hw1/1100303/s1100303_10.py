def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    maxtime=1     #最大連續出現次數設為1
    curtime=1      #現在數字連續出現設為1
    prenum=None  #上一個數字設為none
    
    for i in nums:
        if i==prenum:  #上一個數字和現在的數字相同
            curtime+=1     #連續次數+1
            maxtime=max(curtime,maxtime)  #將目前最大連續值記錄下來  

        else:  #若數字已不連續,重新計算接下來的連續數字次數
            prenum=i  
            curtime=1

    return maxtime #印出最大連續次數

if __name__ == '__main__':
    lst =  [0,0,1,1,1,1,0,0,0,1]

    print(homework_1(lst))
    