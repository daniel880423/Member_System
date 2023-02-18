def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    import copy
    total = 0
    lst1 = copy.deepcopy(lst)
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            lst1[i] += 1
    for i in range(len(lst1)-1):
        if lst1[i+1] <= lst1[i]:
            lst1[i+1] = lst1[i] + 2
    for i in range(len(lst)):
        total += lst1[i] - lst[i]
    return total
if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    