def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    now=[nums[0],1,1]   ##[nums index 0 的值,現在次數,最多次數]   
    for i in nums[1:]:  ##將nums 從 index 1位置跑到尾巴
        if i==now[0]:   ##如果當前index的值等於 now[0]的值
            now[1]+=1   ##now[1]就+1 也就是現在次數+1    
            if now[1]>now[2]: ##如果now[1]>now[2] ,也就是現在次數大於最多次數
                now[2]=now[1] ##將最大次數更新為現在的次數
        else:now[0],now[1]=i,1   ##如果當前index的值不等於now[0]的值，將now[0]更新成當前index的值；現在次數也重設為1
    return now[2]
  
if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))