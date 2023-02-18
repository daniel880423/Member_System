def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    length = len(lst)
    position = 0
    step = 0
    if lst[position] % 2 != 0:
        lst[position] += 1
        step += 1
        position += 1
    else:
        position = 1

    for i in lst[1:]:
        if i <= lst[position-1]:
            lst[position] = lst[position-1] + 2
            step += lst[position] - i
            position += 1

        elif i % 2 != 0:
            lst[position] += 1
            step += 1
            position += 1





    return step

if __name__ == '__main__':
    lst = [2,4,6]
    print(homework_2(lst))
    