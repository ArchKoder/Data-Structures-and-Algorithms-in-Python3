class queue:
    def __init__(self):
        self.q=[]
        self.front,self.rear=-1,-1
    @property
    def size(self):
        return self.rear-self.front
    def enque(self,item):
        self.q.append(item)
        self.rear+=1
    def deque(self):
        if self.size==0:
            return False#Underflow
        temp=self.q[0]
        self.q=self.q[1:]
        self.front+=1
        if self.size==0:
            self.q,self.front,self.rear=[],-1,-1
        return temp

    def copy(self):
        temp=queue()
        for _ in range(self.size):
            t=self.deque()
            temp.enque(t)
            self.enque(t)
        return temp

    def __str__(self):
        out=""
        for _ in range(self.size):
            temp=self.deque()
            out+="|"+str(temp)+" "
            self.enque(temp)
        return out
if __name__ == '__main__':
    q=queue()
    print(q.size)
    q.enque(0)
    q.enque(1)
    q.enque(2)
    print(q,q.size)
    print(q.deque())
    print(q,q.size)
