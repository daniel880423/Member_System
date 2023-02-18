def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    bool = False

    if Str == Str[::-1]:
        bool = True

    return bool

if __name__ == '__main__':
    Str = 'abcdefggfedcba'
    print(homework_4(Str))
    