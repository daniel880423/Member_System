def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    medium = len(Str)//2 #中間
    ans = True
    for i in range(medium):     #確認第一位到中間是否也等於最後一位到中間
        if Str[i] != Str[-i-1]: #如果不是True變False
            ans = False         #如果是依舊是True
            break
    return ans                  

if __name__ == '__main__':
    Str = "AAAAAaaaaa"
    print(homework_4(Str))
    