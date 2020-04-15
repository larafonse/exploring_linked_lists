# Initializing Linked List
class LinkedList:
    # Function to initialize the linked list class
    def __init__(self):
        self.head = None # Initialize the head of linked list as

    # Function to add passed in Node to start linked list
    def addToStart(self, data):
        tempNode = Node(data) # create a new Node with data passed in 
        tempNode.setNextNode(self.head) # set current list to to the next Node of temp node
        self.head = tempNode # set new head as temp node
        del tempNode

    # method displays Linked List
    def display(self):
        start = self.head  

        # check is linked list is empty
        if start is None:
            print("Empty List!!!")
            return False

        # while start is not null print data in null 
        while start:
            print(str(start.getData()), end=" ")
            start = start.next # assign next node to print

            # print arrows if start is not null
            if start: 
                print("-->", end=" ")
        print()


# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

    # Getter for data of node
    def getData(self):
        return self.data

    # Setter for data
    def updateData(self, data):
        self.data = data # Assign data

    # Setter for next node
    def setNextNode(self, node):
        self.next = node # Assign next node

    # Getter for next node
    def getNextNode(self):
        return self.next 
    

    

myList = LinkedList()

# adding some elements to the start of LinkedList
myList.addToStart(5)
myList.addToStart(4)
myList.addToStart(3)
myList.addToStart(2)
myList.addToStart(1)


myList.display()