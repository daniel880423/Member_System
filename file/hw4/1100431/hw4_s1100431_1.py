def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
  if len(str) <= 1:  #邊界條件
        return True
  elif str[0] != str[-1] :
    return False     
  else:
        return str[0] == str[-1] and homework_4(str[1:-1])   #遞迴







  return 

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    