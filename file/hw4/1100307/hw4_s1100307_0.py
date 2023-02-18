def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str)>=2:
        if Str[0]!=Str[-1]:
            return False
        homework_4(Str[1:-1])
    return True
    
    








if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    