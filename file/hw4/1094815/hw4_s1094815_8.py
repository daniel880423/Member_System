def homework_4(Str):
    # 非遞迴解法：
    # return Str == Str[::-1]
    if len(Str)<=1: # 若Str長度小於等於1代表比對結束，回傳True
        return True
    if Str[:2]!=Str[-2:][::-1]: # 若有某組不相同則直接中斷遞迴，回傳False
        return False
    return homework_4(Str[2:-2]) # 下層遞迴