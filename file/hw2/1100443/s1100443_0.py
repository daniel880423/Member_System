def homework_2(lst): 
    total_1=0
    for i in range(len(lst)):
        total_1+=lst[i]

    for i in range(len(lst)):
        if i == 0:
            if lst[i] % 2 != 0:
                lst[i] += 1
        elif i >0:
            if lst[i] > lst[i-1] and lst[i] % 2 != 0:
                lst[i] += 1
            if lst[i] <= lst[i-1] :
                lst[i] = lst[i-1] +2
        
    total_2=0
    for i in range(len(lst)):
        total_2 += lst[i]

    result = total_2 - total_1

    return result

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    