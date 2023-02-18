def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if Str == '':
      return True
    if len(Str)>=10:
        if Str[0]==Str[-1]:
            if Str[1]==Str[-2]:
                if Str[2]==Str[-3]:
                    if Str[3]==Str[-4]:
                        if Str[4]==Str[-5]:
                            Str=Str[5:-5]
                            return (homework_4(Str))
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    if Str[0] == Str[-1]:
        Str = Str[1:-1]
        return homework_4(Str)
    else:
         return False


if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    