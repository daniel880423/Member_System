def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    strlen = len(Str)   #每次進遞迴先算長度
    if strlen > 10000:
        return False
    if strlen == 0:     #若Str已經變為零了，代表是回文數，回傳True
        return True
    now_ascii_value = ord(Str[0])   #將字串裡的第一個字元變成ascii code較好判斷大小寫
    judge_acsii_value = ord(Str[strlen-1])  #也將最後一個字元換成ascii code
    if now_ascii_value == judge_acsii_value:    #比較是否一樣
        Str = Str[1:-1]    #若一樣就將第一個跟最後一個字元從Str刪除
        return homework_4(Str)  #繼續跑遞迴直到strlen=0
    else:
        return False    #若一遇到ascii code值不一樣，代表不可能為回文數，直接回傳False

if __name__ == '__main__':
    Str = "Abccba"
    print(homework_4(Str))
    