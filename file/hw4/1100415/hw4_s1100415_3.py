def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) < 100:
        if len(Str)<2:  #若字串長度小於2(即字串中只有一個字或沒有字)則符合迴文條件
            return True
        if Str[0]!=Str[-1]: #檢查字串頭尾是否相同
            return False
        else: 
            return homework_4(Str[1:-1])    #若字串頭尾相同，則刪除頭尾再執行一次function
    else:
        reverse_string = ''.join(reversed(Str[-100:]))
        if Str[0:100] != reverse_string:
            return False
        else:
            return homework_4(Str[100:-100])
        
        
if __name__ == '__main__':
    Str =   "abba"
    print(homework_4(Str))
    