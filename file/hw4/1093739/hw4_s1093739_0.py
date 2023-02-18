def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

     
      if len(Str) <= 2:#判斷長度是否為2以內
          return True
      if Str[0] != Str[-1]:#判斷第一個字與最後一個字是否相同
          return False
      return homework_4(Str[1:-1])#將第二個字與倒數第二個字返回函數
        
     
     

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    