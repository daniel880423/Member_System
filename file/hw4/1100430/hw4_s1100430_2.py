def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    half = len(Str)//2  #設一半為斷點
    ans = True  #先令答案為真
    for i in range(half):  
        if Str[i] != Str[-i-1]:  #判斷對應位置是否相同
            ans = False  #否的話 答案為假
            break  #跳出
    return ans #回傳

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    