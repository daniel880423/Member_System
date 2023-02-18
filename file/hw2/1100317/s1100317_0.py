def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    l = len(lst)
    s = 0
    
    for i in range(l):
        if (lst[i] % 2) == 0:
            continue
        else:
            lst[i] += 1
            s += 1

    for i in range(l-1):
        if lst[i] < lst[i+1]:
            continue
        if lst[i] == lst[i+1]:
            lst[i+1] = lst[i+1]+2
            s += 2
        else:
            a = lst[i] + 2
            s = s + (a-lst[i+1])
            lst[i+1] = a
    
    return s

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))
    