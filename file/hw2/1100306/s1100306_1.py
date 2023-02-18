def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    len_lst = len(lst)
    total_count = 0
    for i in range(len_lst):
        
        if lst[i] % 2 != 0:
            lst[i] += 1
            total_count += 1
        if i == len_lst-1:
            break
        if lst[i] >= lst[i+1]:
            copy_lst = lst[i+1]
            lst[i+1] = lst[i]+2
            total_count += lst[i+1] - copy_lst
        
    return total_count

if __name__ == '__main__':
    lst = [3]
    print(homework_2(lst))
    