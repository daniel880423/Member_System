def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    l = len(Str)  #算出字串長度
    flag = False      #立flag
    if l>10000:       #如果字串長度>10000
        flag = False   #等於False
    else:             #如果小於10000
        ll = l//2     #將 l除2
        
        count = 0      #計算一樣的有幾次
        for i in range(0,ll):
            if Str[i] == Str[l-1-i]:   #如果一樣count+1
                count += 1
            else:
                count += 0
        if count == l/2:    #如果一樣的次數等於長度除2
            flag = True     
        else:
            flag = False
            








    return flag

if __name__ == '__main__':
    Str = "abba"
    #homework_4(Str)
    print(homework_4(Str))