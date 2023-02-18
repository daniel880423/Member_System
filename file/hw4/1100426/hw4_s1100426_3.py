import sys

sys.setrecursionlimit(5000)
sys.getrecursionlimit()
def homework_4(Str): 
    

    if len(Str)<=0:
        return True
    if Str[0]!=Str[-1]:
        return False
    
    else:
        length = len(Str)
        
        return homework_4(Str[1:-1])








    

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    