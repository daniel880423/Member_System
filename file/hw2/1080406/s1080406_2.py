def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count = 0
    for i in range(len(lst)):
        if (lst[i]+1) % 2 == 0:
            lst[i] += 1
            count += 1

    for i in range(len(lst)-1):
        while lst[i] >= lst[i+1]:
            lst[i+1] += 2
            count += 2
            continue
    return count

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    