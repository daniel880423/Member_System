def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    return len(Str) < 2 or (Str[0] == Str[-1] and homework_4(Str[1:-1]))#字串是0或1回傳True，字串首尾不同回傳False，相同就去掉首尾再呼叫一次
    
if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    