def homework_4(Str): 
   if len(Str) < 8:                    # 如果字串總數小於8
         return Str[::1] == Str[::-1]  # 從字串第一項開始跟最後一項往前比對          
   else :                              # 字串總尚大於或等於8
      if Str[0] != Str[-1] :           # 比對第一項和最後一項  
         return False
      elif Str[1] != Str[-2]:          # 比對第二項和倒數第二項
         return False
      elif Str[2] != Str[-3]:          # 比對第三項和倒數第三項
         return False
                   
   return homework_4(Str[3:-3])        # 刪除字串前三項和後三項

if __name__ == '__main__':
   Str = "abccba"
   print(homework_4(Str))
    