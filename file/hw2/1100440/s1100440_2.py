def homework_2(lst):  # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    now = 0
    step = 0
    if lst[now] % 2 != 0:                      # 處理list的第一個數字
        lst[now] += 1
        step += 1
        now += 1
    else:
        now = 1

    for i in lst[1:]:                               # 處理list第一個以後的數字
        
        if i <= lst[now-1]:
            lst[now] = lst[now-1] + 2
            step += lst[now] - i
            now += 1

        elif i % 2 != 0:
            lst[now] += 1
            step += 1
            now += 1

        elif i % 2 == 0:
            now += 1

    return step


if __name__ == '__main__':
    lst = [2, 6, 1, 2]
    print(homework_2(lst))
