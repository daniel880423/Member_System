def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    len_lst = len(lst)
    total = 0

    for i in range (len_lst):
        total += lst[i]

    for i in range(len_lst):
        if i > 0:
            if (lst[i] - lst[i-1]) > 0 and lst[i] %2 != 0:
                lst[i] += 1
            elif (lst[i] - lst[i-1]) <= 0 :
                lst[i] = lst[i-1] +2
            
        else:
            if lst[i] %2 != 0:
                lst[i] += 1
    
    all = 0
    for i in range (len_lst):
        all += lst[i]
    step = all - total




    return step



if __name__ == '__main__':
    lst = [2,2]
    print(homework_2(lst))
    