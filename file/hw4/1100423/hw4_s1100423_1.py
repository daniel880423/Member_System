def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    len_s= len(Str)+1  
     
    #if len(s)<2:
    len_s = len_s-2  #去掉頭尾長度-2
    if len_s<2:      
        return True
    if Str[0] != Str[-1]:  
        return False
    return palindrome(Str[1:-1])


if __name__ == '__main__':
    Str = "123321"
    print(homework_4(Str))
    