from math import dist

def homework_6(nodes):
    ans=0
    b=0
    distance=[0,0,0,0]
    for i in range(len(nodes)-1):
        a= min(distance)
        if i > 1:
                if a>b:
                    distance=[b]
        ans+=min(distance)
        distance.remove(min(distance))
        if len(distance)>=2:
            b = min(distance)
        del distance[0:4]
        for j in range(i+1,len(nodes)):
            distance+=[abs((nodes[j][0]-nodes[i][0]))+abs((nodes[j][1]-nodes[i][1]))]
            if i == (len(nodes)-2):
                ans+= min(distance)

    return ans

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
