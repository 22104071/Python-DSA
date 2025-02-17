# DOUBLY LINKED LIST
class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
#To create an Empty LinkedList 
class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        print()
        if self.head == None:
            print("LinkedList is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data,'-->',end = " ")
                n = n.nref
    #Reverse Linked List Traversal
    def print_ll_reverse(self):
        print()
        if self.head == None:
            print("LinkedList is empty.")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,'-->',end = " ")
                n = n.pref
#To insert node in Empty link list
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")
#To insert node at beginning
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
#To insert node at the end           
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                n.nref = new_node
                new_node.pref = n
#To insert node after a ceratin node
    def add_after(self,data,x):
        new_node = Node(data)
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given node is not present")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given node is not present")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node
                
#DELETION OPERATION
    def delete_begin(self):
        if self.head == None:
            print("LL is empty!")
            return
        if self.head.nref == None:
            self.head = None
            print("Now DLL is empty!")
        else:
            self.head = self.head.pref
            self.head.pref = None
    def delete_end(self):
        if self.head == None:
            print("LL is empty!")
            return    
        if self.head.nref == None:
            self.head = None
            print("Now DLL is empty!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None
#To delete the node by value
    def delete_byvalue(self,x):
        if self.head == None:
            print("LL is empty!")
            return
        if self.head.nref == None:
            if x == self.head.data:
                self.head = None
                
            else:
                print(x," is not present in the DLL")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            print("Now DLL is empty!")

#Example
dll = LinkedList()
dll.insert_empty(10)
dll.add_begin(20)
dll.add_end(90)
dll.add_after(30,20)
dll.add_before(50,90)
dll.delete_begin()
dll.delete_end()
dll.delete_byvalue(30)
dll.print_ll()
dll.print_ll_reverse()
            
    
    
            
            

        
