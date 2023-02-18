def homework_4(Str):  # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) < 100:                                  #測資是否超過100
        if len(Str) < 2:                                #長度只有1的測資必為回文
            return True
        if Str[0] != Str[-1]:                           #頭尾不一樣則不是回文
            return False
        else:
            return homework_4(Str[1:-1])                #頭尾如果一樣，則慢慢縮減(開始遞迴)
    else:                                               #開始比較超過長度100的測資
        compare_data = ''.join(reversed(Str[-100:]))    #comparre放倒數100筆資料
        if Str[0:100] != compare_data:                  #頭100筆跟尾100筆比較
            return False
        else:                                           #頭100筆跟尾100筆一樣
            return homework_4(Str[100:-100])            #慢慢縮減(開始遞迴)
    


if __name__ == '__main__':
    Str = "A0cc0A"
    print(homework_4(Str))
    


if __name__ == '__main__':
    Str = "A0cc0A"
    print(homework_4(Str))
