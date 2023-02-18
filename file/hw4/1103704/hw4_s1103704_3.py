def homework_4(Str): 
   if len(Str) < 8:             
         return Str[::1] == Str[::-1]            
   else :
      if Str[0] != Str[-1] :        
         return False
      elif Str[1] != Str[-2]:
         return False
      elif Str[2] != Str[-3]:
         return False             
   return homework_4(Str[3:-3]) 


    

if __name__ == '__main__':
   Str = "abccba"
   print(homework_4(Str))
    