def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count_step = 0
    long = len(lst)
    for i in range(long):
        if (lst[i] % 2 != 0):
            lst[i] += 1
            count_step += 1
    
    for i in range(1,long):
        while(lst[i]<=lst[i-1]):
            lst[i] = lst[i]+2
            count_step += 2
            if lst[i]>lst[i-1]:
                break
    
    return  count_step

if __name__ == '__main__':
    lst =[1,5,2,7,4]
    print(homework_2(lst))
    