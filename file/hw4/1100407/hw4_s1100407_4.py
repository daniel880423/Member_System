def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    half = len(Str)//2
    ans = True
    for i in range(0,half,3):
        if Str[i] != Str[-i-1] or Str[i+1] != Str[-i-2] or Str[i+2] != Str[-i-3]:
            ans = False
            break
    return ans

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    