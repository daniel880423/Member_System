def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if Str == "".join(reversed(Str)) :
        return True

    return False

if __name__ == '__main__':
    Str = "abbaabbbbaabba"
    print(homework_4(Str))
    