#stack using singly linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def isEmpty(self):
        return self.top==None
    def push(self,x):
        new_node=Node(x)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        x=self.top.data
        self.top=self.top.next
        return x
    def peek(self):
        if self.top==None:
            return None
        return self.top.data
    def display(self):
        if self.top==None:
            print("Stack is empty")
            return
        temp=self.top
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        print()


stack=Stack()
while True:
    choice=int(input("Enter 1 for push, 2 for pop, 3 for peek, 4 for display and 5 for exit:"))
    if choice==1:
        data=input("Enter data to push:")
        stack.push(data)
    elif choice ==2:
        popped_item=stack.pop()
        if popped_item!=None:
            print(f"Popped element:{popped_item}")
    elif choice==3:
        top_item=stack.peek()
        if top_item==None:
            print("Stack is empty")
            continue
        print(f"Top item:{top_item}")
    elif choice==4:
        stack.display()
    elif choice==5:
        break
    else:
        print("Invalid input")