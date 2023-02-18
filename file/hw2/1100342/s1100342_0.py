def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count =0#計算步數
    pre = 0#記錄前一個值
    for i in lst:
        if i%2 != 0:#非偶數則加一
            i+=1
            count +=1
        
        while i <=pre:#未大於前一個則加二
            i+=2
            count += 2
        pre = i






    return count

if __name__ == '__main__':
    lst = [1,1,1]




    print(homework_2(lst))
    