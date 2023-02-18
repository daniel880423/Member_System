def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    i = int(len(Str)/4)
    if len(Str) < 2:
        return True
    if Str[i-1:0:-1]+Str[0]  != Str[-i:]:
        return False
    return homework_4(Str[i:-i])
    
if __name__ == '__main__':
    Str = 'FuxkkxuF'
    print(homework_4(Str))
    