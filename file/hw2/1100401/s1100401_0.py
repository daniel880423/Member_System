def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    lens = len(lst)
    last = 0
    step = 0
    for i in range(0,lens):
        if lst[i] <= last:
            step+=last+2-lst[i]
            lst[i]=last+2
            last=lst[i]
        elif lst[i]%2 != 0:
            lst[i]+=1
            step+=1
            last=lst[i]
    return step

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    