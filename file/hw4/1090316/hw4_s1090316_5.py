def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    if len(Str) < 2: #如果字串只有0個或1個字元，那麼該字串符合迴文的定義
        return True
        
    return Str[0]+Str[1] == Str[-1]+Str[-2]and homework_4(Str[2:-2]) #字串符的第一項和最後一項等同，所以去除字串的第一項和最後一項，繼續進行檢查

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    