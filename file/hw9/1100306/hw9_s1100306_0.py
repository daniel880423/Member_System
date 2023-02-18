def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    global a
    a = items
    return DFS(bag_size, 0, a[0], 0)

def DFS(size, price, visit, max_price):
    visit = []
    max_price = 0
    h = 1
    for i in a:
        if i[0] > size:
            h += 1
            continue
        visit.append(i)
        for j in a[h:]:
            
                visit.append(j)
                size_total = 0
                for k in visit:
                    size_total += k[0]
                    price += k[1]
                if size_total <= size and price > max_price:
                    max_price = price
                    price = 0
                else:
                    price = 0
                if size_total > size:
                    visit.pop()
                
        visit = []
        h += 1
        

    return max_price

if __name__ == '__main__':
    bag_size = 3
    items = [[1, 25], [4, 120], [4, 30], [1, 130], [2, 20]]
    print(homework_9(bag_size, items))
    # 155
    