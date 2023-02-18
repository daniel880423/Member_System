def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
step = 0
i = 2

lst = [1,1,1]
s_lst = lst
s_lst=lst
if lst[0] % 2 != 0:
    lst[0] = lst[0] + 1
    step += 1
    
if lst[1] < lst[0]:
    step += lst[0] + 2 - lst[1]
    lst[1] = lst[0]+2
else:
    if lst[1] % 2 != 0:
        lst[1] += 1
        step += 1
    
gap = lst[1] - lst[0]
print(len(lst))

for i in range(len(lst)):
    if(lst[i] - lst[i-1] == gap):
        continue
    else:
        save = lst[i-1] + gap
        lst[i] = save

j = 0
for j in range(len(lst)):
    step += lst[j] - s_lst[j]









    return 

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    