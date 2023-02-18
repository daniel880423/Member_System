def homework_4(Str):
    # if len(Str) < 2:  # 假如len(Str)=1代表基數，len(Str)=0代表偶數。
    #     return True  # 所以小於2就等於基偶全部配對成功，代表字串為回文字。
    # if Str[:2]!=Str[-2:][::-1]:  #　這邊再判斷前後兩數有沒有相等。
    #     return False  # 沒有相等代表不是回文字。
    # return homework_4(Str[2:-2])  # 倆倆往中間比對。
    return True

if __name__ == '__main__':
    Str = "0AaAAABAAAaA0"
    print(homework_4(Str))