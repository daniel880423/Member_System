def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    #len_s= len(Str)+1  
     
    
    #len_s = len_s-4  #去掉頭尾長度-2
    #if len_s<2: 
    if len(Str)<2:  
        return True
    if Str[0:2] != Str[-1]+Str[-2]:  
        return False
    return homework_4(Str[2:-2])


if __name__ == '__main__':
    Str = "1233211"
    print(homework_4(Str))
    