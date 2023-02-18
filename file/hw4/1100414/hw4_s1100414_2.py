def homework_4(str1): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(str1)<2:
        return True
    return str1==str1[::-1] and homework_4(str1[2:-2])
            

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))