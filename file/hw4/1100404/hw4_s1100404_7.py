def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if Str == "": #處理到最後剛剛好變成空字串，且中間判斷沒有FALSE，回傳True
        return True
    if len(Str) >= 10: #假如長度大於10
        if Str[0:5] == Str[-1:-6:-1]: #抓前面五個和最後五個(最後五個反轉)
            Str = Str[5:-5] #刪除比較過的10個字
            return homework_4(Str) #再往下一層呼叫函式
        else:
            return False #發現有不一樣的，回傳FALSE
            
    if Str[0] == Str[-1]: #長度比10小，開始第一個與最後一個比較
        Str = Str[1:-1] #刪除比較過的2個字
        return homework_4(Str) #再往下一層呼叫函式
    else:
        return False #回傳FALSE
        
if __name__ == '__main__':
    Str = "abcdefggfedcba"
    print(homework_4(Str))
    