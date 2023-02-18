def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    Str = Str.strip()           #將字串前後的空白剔除
    if len(Str) <= 1:           #如果目前Str的長度小於等於1
        return True

    elif Str[0] != Str[-1]:     #如果目前Str中第一個字不等於最後一個字
        return False


    return homework_4(Str[1:-1])    #將此函式遞迴並且是將目前的字串前後一項剔除

if __name__ == '__main__':
    Str = " abba"
    print(homework_4(Str))
    