def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    if len(Str) < 2: #當Str只剩一位或沒有時,回報True為回文字
        return True
    return Str[0] == Str[-1] and homework_4(Str[1:-1])

if __name__ == '__main__':
    Str = "zb1bz"
    print(homework_4(Str))
    