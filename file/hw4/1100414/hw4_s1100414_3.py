def homework_4(str1): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    return str1==str1[::-1] or len(str1)<2
            

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    