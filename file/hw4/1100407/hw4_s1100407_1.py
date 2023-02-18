def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    lens = len(Str)
    ans = True
    for i in range(0,lens//2,2):
        if Str[i] != Str[-i-1]:
            ans = False
            break
        if Str[i+1] != Str[-i-2]:
            ans = False
            break
    return ans

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    