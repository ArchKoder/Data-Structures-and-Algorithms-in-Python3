class Stack:
    def __init__(self,size=float('inf')):#not mentioning the size gives infinite size stack
        self.size=size
        self.st=[]
    def push(self,data):
        if len(self.st)<size:
            self.st.append(data)
            return True
        return False#overflow
    def pop(self):
        if len(self.st):
            return self.st.pop()
        return False#underflow
    def peek(self):
        if len(self.st):
            return self.st[-1]
        return False#underflow
    def isEmpty(self):
        if len(self.st):
            return False
        return True#empty
        
