from math import radians
from operator import truediv
def homework_4(Str):
    if len(Str)<2: #字串剩下一個，即成功
        return True
    if Str[0]+Str[1]!=Str[-1]+Str[-2]: #前兩位跟後兩位比，如果不同即失敗
        return False
    else:
        return homework_4(Str[2:-2]) #去掉前後兩位並回傳

if __name__ == '__main__':
    Str = "abccba"
    print(homework_4(Str))