def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    n = len(Str)//2
    m = True
    for i in range(n):
        if Str[i] != Str[-i-1]:
            m = False
            break
    return m 







    return 

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    