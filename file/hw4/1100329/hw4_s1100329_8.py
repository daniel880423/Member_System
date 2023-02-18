def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str)<2:return True                         ##如果長度<2，直接回傳1
    if Str[0]!=Str[-1] or Str[1]!=Str[-2] :return False  ##如果對應位置不同，回傳0
    if len(Str)<4:return True ##如果長度<4，直接回傳1
    return homework_4(Str[2:-2])   ##繼續遞迴



if __name__ == '__main__':
    Str = 'abcdefggfedcba'
    print(homework_4(Str))
    