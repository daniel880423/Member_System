def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    

    l = len(Str)
    if l < 2:
        return True
        
    if Str[0:2] != Str[-1] + Str[-2]:
        return False
    return homework_4(Str[1:-1])







if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    