from math import radians
from operator import truediv
def homework_4(Str):
    if len(Str)<2:
        return True
    if Str[0]+Str[1]!=Str[-1]+Str[-2]:
        return False
    else:
        return homework_4(Str[2:-2])

if __name__ == '__main__':
    Str = "abccba"
    print(homework_4(Str))