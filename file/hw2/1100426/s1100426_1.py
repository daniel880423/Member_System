def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    move_nums = 0
    l = len(lst)
    
    for i in range (0,l-1):
        if lst[i]%2 == 1:
            lst[i]+=1
             
            move_nums +=1   #紀錄移動次數
        
        if lst[i] >= lst[i+1]:
            while lst[i]>=lst[i+1]:

                lst[i+1]+=2
                move_nums +=2
           
           
    if lst[l-1]%2 == 1:
        lst[l-1]+=1
        move_nums+=1
        
    return move_nums






    

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    