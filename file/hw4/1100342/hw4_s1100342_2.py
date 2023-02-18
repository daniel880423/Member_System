def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    ll = len(Str)#字串長度
    n = ll//2
    i = n - 1
    if ll%2 ==0:#偶數        
        j = n
    else:#奇數
        j = n + 1
    #從中心開始擴散確認是否為回文
    if isp(Str[i:j+1]):
        return isp(Str[i-1:j+2])
    return False
def isp(Str):
    if Str[0]==Str[-1]:#判斷字首字尾是否相同
        return True








if __name__ == '__main__':
    Str = "aba"
    print(homework_4(Str))
    