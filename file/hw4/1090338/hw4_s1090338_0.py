from math import radians
from operator import truediv
def homework_4(Str):
    times=len(Str)//2 #回圈最低次數
    if times==0:
        return True
    if Str[0]!=Str[-1]:
        return False
    return (homework_4(Str[1:-1]))

if __name__ == '__main__':
    Str = "abtccba"
    print(homework_4(Str))