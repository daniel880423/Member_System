
def homework_4(Str): 
    import sys

    sys.setrecursionlimit(20000)
    sys.getrecursionlimit()

    if len(Str)<=1:
        return True
    if Str[0:2]!=Str[-1]+Str[-2]:
        return False
    
    
        
        
    return homework_4(Str[2:-2])








    

if __name__ == '__main__':
    Str = "abcba"
    print(homework_4(Str))
    