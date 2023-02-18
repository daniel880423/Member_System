def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    T1 = 0
    for i in range(len(lst)):
        T1 += lst[i]

    for i in range(len(lst)):
        if i == 0:
            if lst[i] % 2 != 0:
                lst[i] += 1
        elif i > 0:
            if lst[i] > lst[i-1] and lst[i] % 2 != 0:
                lst[i] += 1
            elif lst[i] <= lst[i-1] :
                lst[i] = lst[i-1] +2
        
    T2 = 0
    for i in range(len(lst)):
        T2 += lst[i]

    final = T2 - T1

    return final 

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
        