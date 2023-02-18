def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    step_count = 0
    index = 1
    for i in range(0,len(lst)):
        if index == len(lst):
            break
        else:
            while lst[index] <= lst[i]:
                lst[index] += 1
                step_count += 1
                if lst[index] < lst[i]:
                    lst[index] += 1
                    step_count += 1
                else:
                    if (lst[index] % 2 != 0 ):
                        lst[index] += 1
                        step_count += 1
                        
                        
                    if lst[index] == lst[i]:
                        lst[index] += 1
                        step_count += 1
                        
                        
                    if lst[i] % 2 != 0:
                        lst[i] += 1
                        step_count += 1
                    
                    
                    #lst[index] += 1
                   
                continue
                    
                    
            if lst[index] % 2 != 0:
                lst[index] += 1
                step_count += 1
            if lst[i] %2 != 0:
                lst[i] += 1
                step_count += 1
                   
               
            index += 1
       
              

    return (step_count)

if __name__ == '__main__':
    lst = [2,4]
    print(homework_2(lst))
    