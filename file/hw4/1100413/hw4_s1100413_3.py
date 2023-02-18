def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    
    
    if len(Str) < 2: #如果字符串只有0個或1個字符，那麽該字符串符合回文的定義
        return True
    
    if Str[0:2]!=Str[-1]+Str[-2]: #如果字符串不止一個字符，那麽檢查字串符的第一項和最後一項是否等同
        return False
    
    
    return homework_4(Str[2:-2])#字串符的第一項和最後一項等同，所以去除字串的第一項和最後一項，繼續進行檢查   

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    