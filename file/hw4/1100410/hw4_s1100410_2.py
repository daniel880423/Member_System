from platform import java_ver


def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    #我分了2種方式討論，一種是字串長度從2~5000的，一種是大於5000的，因為遞迴最多只能2500次
    i =0                                    #設第一個指標i=0         (第一個)         
    j = len(Str)-1                          #設第二個指標j=len(Str)-1(最後一個)
    if len(Str)<5000:                       #如果是字串長度小於5000的
        ans = Check1_Palindromic(Str,i,j)   #會用Check1_Palindromic的方式測試，回傳值設為ans
    
    else:                                   #如果是字串長度大於5000的
        k = len(Str)//2-1                   #設第三個指標k = len(Str)//2-1 (中間靠前的那一個)
        if len(Str)%2==0:                   #設第四個指標l(l要分2種情況判斷)
            l = len(Str)//2                 #如果字串長度能夠整除2，l = len(Str)//2 
        else:
            l = len(Str)//2+1               #不能整除2，l = len(Str)//2+1
        ans = Check2_Palindromic(Str,i,j,k,l)#則進入Check2_Palindromic查看是否為回文字，回傳值設為ans
    
    return ans                      #回傳給主程式(main)
    
def Check1_Palindromic(Str,i,j):
    while(i<=j):                                    #當指標i小於等於指標j，才能進入迴圈(指標i,j是從外層往內測試)
        if Str[i]==Str[j]:                          #如果指標i對應的值等於指標j對應的值
            check = Check1_Palindromic(Str,i+1,j-1) #進行遞迴，而上一層的遞迴會接收到下一層遞迴回傳的值，其值設為check
            if check == False:                      #如果check是False
                return False                        #則會再回傳給上一層遞迴False(第一層的遞迴會回傳給homework_4 False)
            else:                                   #如果沒接收到值(跑完遞迴都沒遇到不同)
                return True                         #則會再回傳給上一層遞迴True(第一層的遞迴會回傳給homework_4 True)
        else:                                       #如果不同
            return False                            #回傳False

def Check2_Palindromic(Str,i,j,k,l):                        #方法與Check1_Palindromic(Str,i,j)相似，但多了指標k,l從內層往外測試
    while(i<=k and l<=j):                                   #指標i要小於等於指標k，指標l要小於等於指標j
        if Str[i]==Str[j] and Str[k]==Str[l]:               #如果指標i=指標j，並且指標k=指標l(內外層測試同時進行)    
            check = Check2_Palindromic(Str,i+1,j-1,k-1,l+1) #以下內容都與Check1_Palindromic(Str,i,j)相同
            if check == False:
                return False
            else:
                return True
        else:                                   
            return False                       
    

if __name__ == '__main__':
    Str = "b"
    print(homework_4(Str))
    