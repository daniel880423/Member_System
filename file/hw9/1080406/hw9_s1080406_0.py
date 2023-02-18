import copy
def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    size = []
    price = []
    for i in range(len(items)):
        size.append(items[i][0])
        price.append(items[i][1])
    
    def backtrack(start_index,bag_size,max_price,nprice,visit):
        if bag_size == 0 or start_index==len(size):
            res.append(copy.deepcopy(visit))
            return 
        for i in range(start_index,len(size)):
            if i > start_index and size[i] > bag_size:
                continue
            if size[i] <= bag_size:
                nprice+=price[i]
                visit.append(price[i])
                if nprice > max_price:
                    max_price = nprice
                backtrack(i+1,bag_size-size[i],max_price,nprice,visit)
                visit.pop()
            
                
    
    res=[]
    start_index = 0
    max_price = 0
    nprice = 0
    visit=[]
    backtrack(start_index,bag_size,max_price,nprice,visit)
    total = []
    for i in range(len(res)):
        total.append(sum(res[i]))
    return max(total)

if __name__ == '__main__':
    bag_size = 25
    items = [[1, 108], [4, 129], [2, 113], [5, 62], [8, 194], [6, 61], [7, 51], [4, 110], [6, 198], [1, 194], [7, 85], [3, 87], [3, 129], [3, 117], [1, 112]]
    print(homework_9(bag_size, items))
    # 155
    