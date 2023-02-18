def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    lasti = 0
    step = 0
    for i in lst:
        if i <= lasti:
            step += lasti + 2 - i
            i = lasti+2        
        elif i%2 != 0:
            step += 1
            i += 1
        lasti = i
    return step



if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    