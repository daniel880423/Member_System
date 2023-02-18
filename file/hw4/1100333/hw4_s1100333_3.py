def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) > 10000:
        return False
    if len(Str) < 2: 
        return True
    Str1=Str[::-1]
    if Str[:20]!=Str1[:20]: 
        return False
    return homework_4(Str[20:-20])

if __name__ == '__main__':
    Str = "adyuda"
    print(homework_4(Str))
    