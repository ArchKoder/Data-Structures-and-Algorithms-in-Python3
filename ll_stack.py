from singly_linked_list import singly_ll
class Stack:
    def __init__(self):
        self.st=singly_ll()
    def push(self,data):
        self.st.insert(data,self.size()+1)
    def size(self):
        return self.st.size()
    def pop(self):
        if self.size():
            p=self.st.access(self.size())
            self.st.remove(self.size())
            return p
        else:
            return False#Underflow
    def peek(self):
        if self.size():
            p=self.st.access(self.size())
            return p
        else:
            return False#Underflow
    def isEmpty(self):
        return not(self.size())

if __name__ == '__main__':
    stack=Stack()
    stack.push(0)
    print(stack.peek(),stack.size())
    for i in range(10):
        stack.push(i)
    while(not stack.isEmpty()):
        print(stack.pop(),stack.size())
