def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    min_time=0                        # 最小步數初始值設為0
    if (lst[0] % 2)!=0:               # 第一個index的值無法被2整除的話代表為奇數
        min_time+=1                   # 因此步數+1
        lst[0]+=1                     # 第一個值也+1
    else:                             # 如果是偶數則跳出迴圈
        pass

    for i in range(1,len(lst)):    
        if ( lst[i] % 2 )== 0:        #偶數
            while lst[i]<=lst[i-1]:   #如果比前一個數還小就一直累計步數 
                min_time+=2           #因為這邊為偶數所以+2還是偶數
                lst[i]+=2
          
        else:                         #奇數
            min_time+=1               
            lst[i]+=1  
            while lst[i]<=lst[i-1]:   #如果比前一個數還小就一直累計步數   
                min_time+=2           #因為這邊為奇數所以+1才會變偶數
                lst[i]+=2 

    return min_time

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    