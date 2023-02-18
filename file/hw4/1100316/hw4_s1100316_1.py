def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str)<2: #假如字串小於2，回傳True
        return True
    if Str[0:101]!=Str[-1:-102:-1]: #假如前100項不等於後100項，回傳False
        return False
    return homework_4(Str[100:-100]) #去除前100和後100項，繼續遞迴比較



if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    