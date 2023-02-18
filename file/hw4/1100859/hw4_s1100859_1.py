def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if Str == '':#處理到最後變成空字串
      return True
    if len(Str)>=10:#假如長度大於10
        if Str[0]==Str[-1]:#第一項和最後一項
            if Str[1]==Str[-2]:#第二項和倒數第二項
                if Str[2]==Str[-3]:#第三項和倒數第三項
                    if Str[3]==Str[-4]:#第四項和倒數第四項
                        if Str[4]==Str[-5]:#中間項
                            Str=Str[5:-5]
                            return (homework_4(Str))
                        else:
                            return False#回傳false
                    else:
                        return False#回傳false
                else:
                    return False#回傳false
            else:
                return False#回傳false
        else:
            return False#回傳false
    if Str[0] == Str[-1]:
        Str = Str[1:-1]
        return homework_4(Str)
    else:
         return False#回傳false


if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    