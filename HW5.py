https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
#HW 5
#Due Date: 12/07/2018, 11:59PM
########################################
#
# Name:
# Collaboration Statement:
#
########################################

# ---Copy your code from labs 9 and 10 here (you can remove their comments)  



#----- HW5 Graph code     
class Graph:
    def __init__(self, graph_repr=None):
        if graph_repr is None:
            self.vertList = {}
        else:self.vertList = graph_repr

    def addVertex(self,key):
        if key not in self.vertList:
            self.vertList[key] = []
            return self.vertList

    def addEdge(self,frm,to,cost=1):
        if frm not in self.vertList:
            self.addVertex(frm)
        if to not in self.vertList:
            self.addVertex(to)
        self.vertList[frm].append((to, cost))
        return self.vertList

    def bfs(self, start):
    	# Your code starts here

    def dfs(self, start):
    	# Your code starts here


    ### EXTRA CREDIT, uncomment method definition if submitting extra credit
    
    #def dijkstra(self,start):
        # Your code starts here