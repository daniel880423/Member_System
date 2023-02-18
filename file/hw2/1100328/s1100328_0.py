def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    temp = lst[0]
    step = 0
    for i in range(len(lst)):
        if (lst[i]%2 != 0 and lst[i]>=temp):
            step+=1
            lst[i]+=1
        elif lst[i]<temp:
            step+=(temp+2-lst[i])
            lst[i]=temp+2
        temp=lst[i]
    return step





    return 

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))
    