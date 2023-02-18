def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count = 0
    i = 1
    if lst[0] % 2 != 0:
        lst[0]+=1
        count+=1
    last = lst[0]
    while i < len(lst):
        if lst[i] <= last:
            count += last + 2 - lst[i]
            lst[i] = last + 2
        if lst[i] %2 != 0:
            lst[i]+=1
            count+=1
        last = lst[i]
        i+=1
    return count

if __name__ == '__main__':
    lst = [2, 2]
    print(homework_2(lst))
    