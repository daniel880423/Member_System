def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    time=1                          ##time記錄當前次數 預設為1
    maxtime=1                       ##maxtime紀錄累積最多次數 預設為1
    while nums!=[]:                 ##如果傳入的nums這個list不為空就持續地進入
        if len(nums)>1:             ##計算nums這個list的長度是否大於1
            if nums[0]!=nums[1] :   ##如果list index 0與 index1 值不同，就將time重設為1
                time=1
            else:                   ##值同 time +1
                time+=1
            if maxtime<time:        ##如果maxtime小於 time 
                maxtime=time        ##將maxtime的數值改為time的數值
        nums.pop(0)                 ##將list的頭刪掉
    return maxtime                  ##回傳maxtime 也就是回傳累積的最多次數
  
if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))