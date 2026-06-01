class Stack:
    def __init__(self,size):
        self.size=size
        self.stk=[None]*size
        self.top=-1
    def isFull(self):
        return self.top==self.size-1
    def isEmpty(self):
        return self.top==-1
    def push(self,x):
        if self.isFull():
            print("Stack is full")
            return
        self.top+=1
        self.stk[self.top]=x
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        x=self.stk[self.top]
        self.top-=1
        return x
    def peek(self):
        if self.isEmpty():
            return None
        return self.stk[self.top]

def check_bracketSequence():
    bracket_sequence=input("Enter bracket sequence:")
    stack=Stack(len(bracket_sequence))

    for ch in bracket_sequence:
        if ch=="(" or ch=="{" or ch=="[":
            stack.push(ch)
        elif ch==")":
            if stack.isEmpty() or stack.peek()!="(":
                return False
            stack.pop()
        elif ch=="}":
            if stack.isEmpty() or stack.peek()!="{":
                return False
            stack.pop()
        elif ch=="]":
            if stack.isEmpty() or stack.peek()!="[":
                return False
            stack.pop()
    return stack.isEmpty()
value=check_bracketSequence()
if value:
    print("The bracket sequence is valid")
else:
    print("The bracket sequence is not valid")