def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    pali = True                          #預設一個變數用來儲存回文數的布林值
    for i in range(len(Str)//2):         #使用for迴圈依次判斷字串第n項和倒數第n項    
        if Str[i] != Str[-i-1]:          #使用if判斷字串第n項和倒數第n項是否不同 
            pali = False                 #若有任一項不同，則不為回文數，將布林值設為False
            break                        #離開迴圈

    return pali                          #回傳布林值   

if __name__ == '__main__':
    Str = "Abba"
    print(homework_4(Str))
    