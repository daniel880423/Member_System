def homework_2(lst): 
    total_1 = 0
    for i in range(len(lst)):
        total_1+= lst[i]

    for i in range(len(lst)):
    
        if i >0:
            if lst[i] > lst[i-1] and lst[i] % 2 != 0:
                lst[i] += 1
            elif lst[i] < lst[i-1] and lst[i] % 2!=0:
                lst[i] = lst[i-1] + 2
            elif lst[i] < lst[i-1] and lst[i] % 2==0:
                lst[i] = lst[i-1] + 2
        else:
            if lst[i] % 2 != 0:
                lst[i] +=1
                
    total = 0
    for i in range(len(lst)):
        total+= lst[i]

    step = total - total_1

    return step

    