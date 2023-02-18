def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    step = 0                         #計算步數
    le =len(lst)                     #lst的長度
    pre_num =lst[0]                  
    if pre_num % 2 != 0:             #若第0個數不是偶數
        pre_num += 1                 #+1即為偶數
        lst[0]= pre_num              #將更改完的數值存回去
        step += 1                    #步數+1

    for i in range(1 , le):
        
        if lst[i] > pre_num and lst[i] % 2 == 0:      #若目前的數比前一個數大且為偶數
            pre_num = lst[i]                          #將前一個數改為目前的數
            
              
        else:
            if lst[i] <= pre_num :          #若目前的數小於等於前一個數
                p = pre_num - lst[i]        #將前一個數減目前的數
                step += p                   #計算入步數
                lst[i] = pre_num            #將前一個數的數值覆蓋到目前的數                                                             
                lst[i] += 2                 #因前一個數一定為偶數，故目前的數要再+2
                step += 2                   #步數+2
                pre_num = lst[i]                                              
            elif lst[i] % 2 != 0:           #若目前的數不是偶數，但大於前一個數
                lst[i]+=1                   #+1即為偶數
                pre_num = lst[i]            
                step += 1                   #步數+1
    return step

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    