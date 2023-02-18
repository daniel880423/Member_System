def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    l=len(Str)-1
    if  l<=1:
        return 1
    elif Str[0]==Str[-1]:
        s=Str[1:l]
        return homework_4(s)
    else:
        return 0






     

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    