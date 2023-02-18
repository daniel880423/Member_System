def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str)<2:
        return True
    if Str[0:10]!=Str[-1:-11:-1]:
        return False
    return homework_4(Str[10:-10])

    








if __name__ == '__main__':
    Str = "abcdefggfedcba"
    print(homework_4(Str))
    