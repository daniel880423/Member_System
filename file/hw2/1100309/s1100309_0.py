def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    times = 0
    
    for i in range(len(lst)):                      #先判斷list裡的數是否為偶數，如果不是則加1變成偶數
        if (lst[i] % 2 != 0):
            lst[i] += 1
            times += 1
    
    for i in range (1,len(lst)):                   #若下一個數小於或等於上一個數，則加2
        while(lst[i] <= lst[i-1]):
            lst[i] += 2
            times += 2
            
    
    return  times

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    