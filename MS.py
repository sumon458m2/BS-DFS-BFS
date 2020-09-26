
def mergesort(a):
    if len(a)>1:
        mid=len(a)//2
        L=a[:mid]
        R=a[mid:]
        mergesort(L)
        mergesort(R)
        a.clear()
        while len(L)>0 and len(R)>0:
            if L[0] <= R[0]:
                a.append(L[0])
                L.pop(0)
            else:
                a.append(R[0])
                R.pop(0)

        for i in L:
            a.append(i)
        for i in R:
            a.append(i)

a=[1,4,3,6,7,8,9,11,23,43,23,5]
mergesort(a)
print(a)


a=[ ]
n=int(input("enter the number:"))
for i in range(0,n):
    a.append(int(input("enter the number:")))
mergesort(a)
print(a)


from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,U,V):
        self.graph[U].append(V)
    def DFSUtil(self,V,visited):
        visited[V]=True
        print(V,end=" ")
        for i in self.graph[V]:
            if visited[i]==False:
                self.DFSUtil(i,visited)
    def DFS(self,V):
        visited=[False]*(max(self.graph)+1)
        self.DFSUtil(V,visited)
g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print("following is DfS from(starting from vertex 2)")
g.DFS(2)

from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,U,V):
        self.graph[U].append(V)
    def BFS(self,S):
        visited=[False]*(len(self.graph))
        queue=[]
        queue.append(S)
        visited[S]=True
        while queue:
            S=queue.pop(0)
            print(S,end=" ")
            for i in self.graph[S]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print("following is BFS from(starting from vertex 2)")
g.BFS(2)


def binary_search(arr,L,r,x):
    if r>=L:
        mid=L+(r-L)//2
        if arr[ mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,L,mid-1,x)
        else:
            return binary_search(arr,mid+1,r,x)
    else:
        return -1
arr=[2,4,56,7,8,9,21,34,34,1,3,5,6]
x=2
result=binary_search(arr,0,len(arr)-1,x)
if result !=-1:
    print("found")
else:
    print("not found")