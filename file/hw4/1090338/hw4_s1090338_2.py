from math import radians
from operator import truediv
def homework_4(Str):
    times=len(Str)//2  #回圈最低次數
    ans=Str[1:-1]
    if times==0:
        ans=True
        return ans
    if Str[0]!=Str[-1]:
        return ans
    return (homework_4(ans))

if __name__ == '__main__':
    Str = "abccba"
    print(homework_4(Str))