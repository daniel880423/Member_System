def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count = 0
    len_ = len(lst) - 1
    
    for i in range(0,len_):
        if lst[i] % 2 == 1:  # 判斷是否為偶數
            lst[i] = lst[i] + 1
            count += 1
            if lst[i] < lst[i+1]:
                continue
            if lst[i] >= lst[i+1]:  # 判斷是否大於下一項
                count += (lst[i]+2) - lst[i+1]
                lst[i+1] = (lst[i]+2)

        else:
            if lst[i] < lst[i+1]:
                continue
            if lst[i] >= lst[i+1]:  # 判斷是否大於下一項
                count += (lst[i]+2) - lst[i+1]
                lst[i+1] = (lst[i]+2)


    return count

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    