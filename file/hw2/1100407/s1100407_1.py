def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count = 0
    last = 0 
    for i in lst:
        while i % 2 != 0:
            i+=1
            count+=1
        while i <= last:
            i+=2
            count+=2
        last = i
    return count

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    