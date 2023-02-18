def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str)<2:#若字串長度只有1或0，回傳True
        return True
    if Str[0]!=Str[-1]:#判斷字首字尾是否相同
        return False
    #若相同，遞迴回傳刪除字首字尾後的字串
    return homework_4(Str[1:-1])







    return 

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    