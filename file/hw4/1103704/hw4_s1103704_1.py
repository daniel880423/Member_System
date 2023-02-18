def homework_4(Str): 
    if len(Str) < 2:             #字串裡面個數小於2的時候
        return True              #回串True
    if Str[0]!=Str[-1]:          #如果Str[0]不等於Str[-1]
        return False             #回傳False
    return homework_4(Str[1:-1]) #刪除第一個和最後一個數字或字母


    

if __name__ == '__main__':
    Str = "abccca"
    print(homework_4(Str))
    