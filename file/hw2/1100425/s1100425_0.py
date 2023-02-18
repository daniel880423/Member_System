def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    step = 0
    if lst[0] % 2 == 1:
        lst[0] = lst[0] + 1
        step = step + 1

    for i in range(1, len(lst)):
        while (lst[i] % 2 == 1 or lst[i] <= lst[i - 1]):
            lst[i] = lst[i] + 1
            step = step + 1 

    return step

if __name__ == '__main__':
    lst =  [1,5,2,7,4]
    print(homework_2(lst))
    