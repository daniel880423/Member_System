def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    l=len(Str)
    if  l<=1:
        return 1
    elif Str[0:1000]==Str[-1:-1001:-1]:
        s=Str[1000:l-1000]
        return homework_4(s)
    else:
        return 0






     

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    