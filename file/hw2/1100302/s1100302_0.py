def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    time = len(lst)
    count = 0
    for i in range(time-1):
        if lst[i] % 2 != 0:
            lst[i] +=1
            count +=1
        if lst[i+1] % 2 != 0:
            lst[i+1] +=1
            count +=1
        n = even(lst[i],lst[i+1])
        count += n
        lst[i+1] +=n





    return count 
def even(a,b):
    count = 0
    if a == b:
        count+=2
    if a > b:
        count = a-b+2
    return count 

    
if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))
    