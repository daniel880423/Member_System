def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) < 2:
        return True
    if Str[0] != Str[-1]:
        return False
    if Str[1] != Str[-2]:
        return False    
    return homework_4(Str[1:-1])






    

if __name__ == '__main__':
    Str = "A0cc0A"
    print(homework_4(Str))
    