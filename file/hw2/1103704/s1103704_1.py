def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    a = 0               #定義一個值來跟
    c = len(lst)
    sum = 0
    for i in range (c):
        if i == 0:
            if (lst[i] % 2) == 0 :
                lst[i] = lst[i]
            else:
                lst[i] = lst[i]+1
                sum = sum + 1 
        else:    
            if lst[i] > lst[i-1] :
                if (lst[i] % 2) == 0 :
                    lst[i] = lst[i]  
                else:
                    lst[i] = lst[i]+1
                    sum = sum + 1 
            elif lst[i] <= lst[i-1] :
                if (lst[i-1] % 2) == 0 :
                    lst[i-1] = lst[i-1]+2
                    sum = sum+lst[i-1]-lst[i]
                    lst[i] = lst[i-1]               
                else:
                    lst[i-1] = lst[i-1]+1
                    sum = sum + lst[i-1]-lst[i]
                    lst[i] = lst[i-1]           
    return sum

if __name__ == '__main__':
    lst = [2]
    print(homework_2(lst))
    