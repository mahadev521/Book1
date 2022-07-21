def getJosephusPosition(n, m):
    class Node:
        def __init__(self, data = None, next = None):
            self.setData(data)
            self = next
        #method for setting the data field of the node 
        def setData(self,data):
            self.data = data
        #method for getting the data field of the node 
        def getData(self):
            return self.data
        #method for setting the next field of the node
        def setNext(self,next):
            self.next = next
        #method for getting the next field of the node 
        def getNext(self):
            return self.next
        #returns true if the node points to another node
        def hasNext(self):
            return self.next != None
    answer = []
        # initialize circular linked list
    head = Node(0)
    prev = head
    for n in range(1, n):
        currentNode = Node(n)
        prev = currentNode
        prev = head # set the last node to point to the front (circular list)
    currentNode = head
    counter = 0
    while currentNode.next != currentNode:
        counter += 1
        if counter == m:
            counter = 0
            prev = currentNode.next
            answer.append(currentNode.data)
        else:
            prev = currentNode
        currentNode = currentNode.next
    answer.append(currentNode.data)
    return answer

print(getJosephusPosition(6, 3))