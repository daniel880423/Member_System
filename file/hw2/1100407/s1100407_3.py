def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count = 0
    if lst[0] % 2 != 0:
        lst[0]+=1
        count+=1
    for i in range(1,len(lst)):
        if lst[i] <= lst[i-1]:
            count += lst[i-1] + 2 - lst[i]
            lst[i] = lst[i-1] + 2
        if lst[i] %2 != 0:
            lst[i]+=1
            count+=1
    return count

if __name__ == '__main__':
    lst = [2, 2]
    print(homework_2(lst))
    