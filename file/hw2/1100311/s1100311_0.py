def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    a = 0
    l = len(lst)
    if lst[0] // 2 != 0:
        lst[0] = lst[0] +1
        a += 1
    for i in  range(1,l):
        while lst[i]>=lst[i-1]:
            lst[i] += 1
            a += 1
        if lst[i] // 2 != 0:
            lst[i] = lst[i] + 1
            a+= 1

   



    return a

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    