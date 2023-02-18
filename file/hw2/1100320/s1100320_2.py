def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    len_lst = len(lst)             #令len_lst為lst的長度
    i = 0                          #令i為lst的index
    step = 0                       #令step為最小步數

    if (lst[0]%2) != 0:            #如果lst中index 0的數字不是偶數
            lst[0] += 1            #把index 0的數字加1變成偶數
            step += 1              #最小步數加1

    while i < len_lst-1:           #當i小於lst的長度-1即進入迴圈
        if lst[i+1] > lst[i]:      #如果index i+1的數字大於index i的數字
            if (lst[i+1]%2) != 0:  #如果index i的數字不是偶數
                lst[i+1] += 1      #把index i的數字加1變成偶數
                step += 1          #最小步數加1
                
        elif lst[i+1] < lst[i]:    #如果index i+1的數字小於index i的數字
            past = lst[i+1]        #把原本index i+1的數字存到past
            lst[i+1] = lst[i] + 2  #把index i+1的數字更新為index i的數字加2
            step += lst[i+1] - past#最小步數加上(更新後index i+1的數字減掉past)
             
        else:                      #index i+1的數字等於index i的數字
            lst[i+1] = lst[i] + 2  #把index i+1的數字更新為index i的數字加2
            step += 2              #最小步數加2
        
        i+=1                       #i每跑完一次迴圈加1
    
    return step                    #回傳最小步數

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))
    