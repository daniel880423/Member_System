def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    str_len = len(Str)
    if str_len <= 1 :
        return True
    elif str_len > 10000:
        return True
    else:
        return Str[0] == Str[-1] and homework_4(Str[1:-1])
       


if __name__ == '__main__':
    Str = "FuxkkxuF"
    print(homework_4(Str))
    