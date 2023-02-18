def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    i =0                            #第0項(指標1)
    j =(len(Str)-1)                 #Str的最後1項(指標2)
    ans = Check_Palindromic(Str,i,j)#進入Check_Palindromic查看是否為回文字，回傳值設為ans
    return ans                      #回傳給主程式(main)
    
    
def Check_Palindromic(Str,i,j):                 #用來查看是否為回文字
    while(i<j):                                 #指標1要小於指標2
        if Str[i]==Str[j]:                      #如果第i項=第j項
            check = Check_Palindromic(Str,i+1,j-1)#進行遞迴，i(指標1)往後1格，j(指標2)往前1格，將迴遞的回傳值設為check
            #(以下if else為遞迴停止後執行,停止有兩種情形,第一種:指標1不等於指標2,第二種:跑到最後，指標1都等於指標2)
            if check == False:                  #如果有被回傳到False(第一種)
                return False                    #回傳False(從最後的遞迴一直往前一個遞迴回傳，最後會回傳到homework_4)
            else:                               #如果沒有(第二種)
                return True                     #回傳True(從最後的遞迴一直往前一個遞迴回傳，最後會回傳到homework_4)

        else:                                   #在遞迴途中，如果第i項(指標1)不等於第j項(指標2)
            return False                        #回傳False(遞迴則停止)


if __name__ == '__main__':
    Str = "ABccba"
    print(homework_4(Str))
    