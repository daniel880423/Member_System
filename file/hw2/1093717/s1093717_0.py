def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    steps = 0
    for i in range(len(lst)):
        if(i == 0):
            if(lst[i]%2!=0):
                lst[i] += 1
                steps += 1
        else:
            if(lst[i]>lst[i-1] and lst[i]%2!=0):
                lst[i] += 1
                steps += 1
            elif(lst[i]<lst[i-1] and lst[i]%2!=0):
                a = lst[i-1] + 2
                steps += a-lst[i]
                lst[i] = a
            elif(lst[i]==lst[i-1]):
                a = lst[i-1] + 2
                steps += a-lst[i]
                lst[i] = a
    return steps

if __name__ == '__main__':
    lst = [2,2]
    print(homework_2(lst))
    