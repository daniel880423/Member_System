def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) < 2: 
        return True
    if Str[0] != Str[-1]: 
        return False
    return homework_4(Str[1:-1])#字串長度是0或1回傳True,不是1就檢查首尾,相同就去掉首尾再呼叫一次
if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    