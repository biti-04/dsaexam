class Stack:
    def __init__(self):
        self.stack = []
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
#to create a stack and add elements
nums = Stack()
nums.push(1)
nums.push(2)
nums.push(3)
nums.push(4)
print("Stack : ",nums.stack)

#to pop an element from the stack
print("Pop : ", nums.pop())
