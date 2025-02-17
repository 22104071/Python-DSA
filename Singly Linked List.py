
#To create a node
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
#To create an Empty LinkedList 
class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head == None:
            print("LinkedList is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data,'-->',end = " ")
                n = n.ref
            print(" ")
#To add a new node at the beginning
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
#To add a new node at the end
    def add_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref #Incrementation part
            n.ref = new_node
#To insert element after a certain node
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("The node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
#To insert element before a certain node
    def add_before(self,data,x):
        if self.head is None:
            print("LinkedList is empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None: #To not traverse beyond last node
            if n.ref.data == x: #To traverse to given node
                break
            n = n.ref # Increment
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
#To add node in empty LL
    def add_empty(self,data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")
#To delete the initial node
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.ref
#To delete the last node
    def delete_end(self):
        if self.head == None:
            print("Linked List is empty")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
#To delete the any given node
    def delete_byvalue(self,x):
        if self.head == None:
            print("Linked List is empty")
        else:
            if x == self.head.data: # To delete 1st node
                self.head = self.head.ref
            n = self.head
            while n.ref is not None:
                if x == n.ref.data:
                    break
                n=n.ref
                if n.ref == None:
                    print('Node is not found')
                else:
                    n.ref = n.ref.ref
#Example
LL1 = LinkedList()
LL2 = LinkedList()

LL1.add_begin(40)
LL1.add_end(100)
LL1.add_after(200,100)
LL1.add_empty(20)
LL1.add_end(500)
LL1.add_before(400,500)
LL1.add_begin(30)
LL2.add_empty(10)

LL1.delete_begin()
LL1.delete_end()
LL1.delete_byvalue(200)

LL1.print_LL()
LL2.print_LL()

        
