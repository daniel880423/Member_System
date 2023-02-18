def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    min=0
    if (lst[0]%2)!=0:
        lst[0]=lst[0]+1
        min+=1

    for i in range(1,len(lst)):
        t=lst[i-1]-lst[i]
        if t>2:
            min+=t+2
            lst[i]=lst[i-1]+2
        elif t<2 and (t%2)!=0:
            min+=1
            lst[i]=lst[i]+1


    return min

if __name__ == '__main__':
    lst = [10, 20, 25, 10, 23, 35, 44, 45, 23, 12]
    print(homework_2(lst))
    print(lst)
    