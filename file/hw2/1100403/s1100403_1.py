def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    i = 0
    length = len(lst)
    step = 0
    
    while i <= length-1:
        if (lst[i]%2 != 0):
            lst[i]+=1
            step+=1
        if (i>0)&(lst[i]<=lst[i-1]):
            step+=(lst[i-1]-lst[i]+2)
            lst[i]=lst[i-1]+2
        i+=1
    
    return step

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))
    