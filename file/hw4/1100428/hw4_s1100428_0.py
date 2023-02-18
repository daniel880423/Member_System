def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    half = len(Str)//2   #將整個字元分成兩半
    ans = True
    for i in range(half): #用迴圈重複執行
        if Str[i] != Str[-i-1]: #判斷第一個跟最後一個是否相等以此類推
            ans = False 
            break
    return ans 

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    