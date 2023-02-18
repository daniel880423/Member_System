def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count = 0
    if (lst[0]+1) % 2 == 0:
        lst[0] += 1
        count += 1
    for i in range(len(lst)-1):
        now = 0
        if lst[i] >= lst[i+1]:
            now = lst[i+1]
            lst[i+1] = lst[i] + 2
            count += lst[i+1] - now
        else:
            if lst[i+1] % 2 == 1:
                lst[i+1] += 1
                count += 1
    return count

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    