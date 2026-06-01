class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def createSinglyLinkedList(self):
        data=input("Enter data for the first Node:")
        if data=="" or data=="None":
            return
        self.head=Node(data)
        temp=self.head
        while True:
            ans=input("Do you want to create another node?(y/n):")
            if ans=='N' or ans=='n':
                return
            data=input("Enter data to create another node:")
            temp.next=Node(data)
            temp=temp.next
    def insertBeforeFirstNode(self):
        data=input("Enter data to insert at first position:")
        temp=Node(data)
        temp.next=self.head
        self.head=temp
    def insertAfterLastNode(self):
        data=input("Enter data to insert at last position:")
        if self.head==None:
            self.head=Node(data)
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=Node(data)
    def insertAfterSpecificNode(self,value):
        data=input(f"Enter data to insert after {value}:")
        temp=self.head
        while temp!=None and temp.data!=value:
            temp=temp.next
        if temp==None:
            print("Value not found!")
            return
        new_node=Node(data)
        new_node.next=temp.next
        temp.next=new_node
    def displaySinglyLinkedList(self):
        if self.head==None:
            print("Linked list is empty")
            return
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
    def search(self,value):
        temp=self.head
        while temp!=None:
            if temp.data==value:
                return True
            temp=temp.next
        return False
    def deleteFirstNode(self):
        if self.head==None:
            print("Linked list is empty")
            return
        self.head=self.head.next
    def deleteLastNode(self):
        if self.head==None:
            print("Linked list is empty")
            return
        if self.head.next==None:
            self.head=None
            return
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
    def deleteSpecificNode(self,value):
        if self.head==None:
            print("Linked list is empty")
            return
        if self.head.data==value:
            self.head=self.head.next
            return
        temp=self.head
        while temp.next!=None and temp.next.data!=value:
            temp=temp.next
        if temp.next==None:
            print("Value not found!")
            return
        temp.next=temp.next.next
    def countNodes(self):
        count=0
        temp=self.head
        while temp!=None:
            count+=1
            temp=temp.next
        return count
    def reverseSinglyLinkedList(self):
        curr=self.head
        prev=None
        while curr!=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        self.head=prev
    def insertAtPos(self,pos):
        temp=self.head
        count=self.countNodes()
        if pos<1 or pos>count+1:
                print(f"Invalid position")
                return
        if pos==1:
            data=input(f"Enter data to insert at position {pos}:")
            new_node=Node(data)
            new_node.next=temp
            self.head=new_node
            return
        for i in range(1,pos-1):
            temp=temp.next

        data=input(f"Enter data to insert at position {pos}:")
        new_node=Node(data)
        next_node=temp.next
        temp.next=new_node
        new_node.next=next_node
    def deleteAtPos(self,pos):
        temp=self.head
        count=self.countNodes()
        if pos<1 or pos>count:
            print("Invalid position")
            return
        if pos==1:
            self.head=self.head.next
            return
        for i in range(1,pos-1):
            temp=temp.next

        n=temp.next
        temp.next=n.next
        n.next=None
        
l1=LinkedList()
l1.createSinglyLinkedList()
l1.insertBeforeFirstNode()
l1.insertAfterLastNode()
l1.insertAfterSpecificNode("20")
l1.deleteFirstNode()
l1.deleteLastNode()
l1.deleteSpecificNode("30")
print(l1.search("20"))
l1.displaySinglyLinkedList()
print(l1.countNodes())
l1.reverseSinglyLinkedList()
l1.displaySinglyLinkedList()
pos1=int(input("Enter position to insert data in linked list:"))
l1.insertAtPos(pos1)
pos2=int(input("Enter position to delete data in linked list:"))
l1.deleteAtPos(pos2)    
l1.displaySinglyLinkedList()