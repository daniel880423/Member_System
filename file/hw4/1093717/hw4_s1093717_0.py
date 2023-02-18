def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) < 2: #如果字串只有0個或1個字元，那麼該字串符合迴文的定義
        return True
    if Str[0]!=Str[-1]: #如果字串不止一個字元，那麼檢查字串符的第一項和最後一項是否等同
        return False
    return homework_4(Str[1:-1])

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    