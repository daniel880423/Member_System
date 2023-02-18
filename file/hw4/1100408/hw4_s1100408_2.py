import sys
sys.setrecursionlimit(5000)
def homework_4(Str): 
    if len(Str)<2:          #長度0或1代表不用判斷了
        return True
    elif Str[0]!=Str[-1]:   #第一項不等於最後一項(False)
        return False
    else:
        return homework_4(Str[1:-1])    #遞迴並且把頭尾刪掉

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    