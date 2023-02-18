def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    pw=[]
    itemss=[]
    New_items=[]

    global maxprofit
    
    for i in range(len(items)):
        if (items[i][0]<=bag_size):
           # print(items[i][0],i,items[i])
            itemss.append(items[i]) 
    for i in range(len(itemss)):
        pw.append([itemss[i][1]/itemss[i][0],i])       
    pw.sort()
    for i in range(len(itemss)):
        New_items.append(itemss[pw[i][1]])
    New_items.reverse()
    New_items.insert(0, [0,0])
  #  print(New_items)
    #=================================
    bestset=[False]*len(New_items)
  #  print(bestset)
    
    
    maxprofit=0
    weight=0
    profit=0
    knapsack (0, profit, weight, bag_size, bestset, New_items)
    return maxprofit

def knapsack (i, profit, weight, bag_size, bestset, New_items):
    global maxprofit
 #   print('profit,',profit)
 #   print('weight',weight)
    if (weight<=bag_size and profit>maxprofit):
  #      print("==================")
        maxprofit=profit
  #      numbest=i
        bestset[i]=True
 #   print('maxprofit',maxprofit)
    
    if (promising(i,profit, weight, bag_size, bestset, New_items)):
 #       print("\n")
 #       print("walk",i+1,1)
        knapsack (i+1,profit+New_items[i+1][1],weight+New_items[i+1][0],bag_size, bestset, New_items)
 #       print("\n")
 #       print("walk",i+1,2)
        knapsack (i+1,profit,weight,bag_size, bestset, New_items)

def promising(i,profit, weight, bag_size, bestset, New_items):
    global maxprofit
    totalweight=0
    bound=0.0
    
    if (weight>=bag_size):
        return False
    else:
        j=i+1
        bound=profit
        totalweight=weight
        while (j<=len(New_items)-1 and totalweight+New_items[j][0]<=bag_size):
            totalweight=totalweight+New_items[j][0]
 #           print(totalweight)
            bound=bound+New_items[j][1]
 #           print(bound)
            j=j+1
 #           print(j)
        k=j
        
        if (k<=len(New_items)-1):
            bound=bound+(bag_size-totalweight)*New_items[k][1]/New_items[k][0]
  #          print("bound",bound)
        return bound>maxprofit
if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
   # items=[[2,40],[5,30],[10,50],[5,10]]
    print(homework_9(bag_size, items))
    # 155
    