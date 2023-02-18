def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count = 0
    if lst[0] %2 !=0:
        lst[0]+=1
        count+=1
    for i in range(1,len(lst)):
        if lst[i]>lst[i-1] and lst[i]%2!=0:
            lst[i]+=1
            count +=1
        else:
            count += lst[i-1]-lst[i]+2
            lst[i] = lst[i-1]+2
    return count

if __name__ == '__main__':
    lst = [2,4,6,8]
    print(homework_2(lst))
    