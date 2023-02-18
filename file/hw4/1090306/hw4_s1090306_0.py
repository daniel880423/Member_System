def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    if len(Str) < 2: #當Str只剩一位或沒有時,回報True為回文字
        return True
    elif Str[0] != Str[-1]: #如果第一個字母和最後一個字母不同時則回報False
        return False
    else: 
        return homework_4(Str[1:-1]) #取第一位到最後一位之間的字母

if __name__ == '__main__':
    Str = "zb1bz"
    print(homework_4(Str))
    