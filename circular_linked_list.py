class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return str(self.data)


class circular_ll:
    def __init__(self,data=None):
        self.head=data if type(data) == type(node()) else node(data)
        if data is None:
            self.head = None
            self.size=0
        if self.head:
            self.head.next=self.head

    def size(self):
        if not self.head:
            return 0
        temp=self.head.next
        size=1
        while(temp is not self.head):
            size+=1
            temp=temp.next
        return size
    def insert(self,data,pos=1):
        noob=data if type(data) == type(node()) else node(data)
        if pos==1 or self.head is None:
            noob.next=self.head
            if not self.head:
                noob.next=noob
                self.head=noob
            else:
                temp=self.head
                while(temp.next!=self.head):
                    temp=temp.next
                temp.next=noob
                self.head=noob
        else:
            pos-=2
            temp=self.head
            while(pos):
                temp=temp.next
                pos-=1
            noob.next=temp.next
            temp.next=noob
            if not noob.next:
                noob.next=self.head
    def __str__(self):
        if self.head:
            out=str(self.head)+"->"
        temp=self.head.next
        if temp:
            while temp is not self.head:
                out+=str(temp)+"->"
                temp=temp.next
        out+="HEAD"
        return out
    def remove(self,pos):
        if pos==1:
            temp=self.head.next
            if temp:
                while temp.next is not self.head:
                    temp=temp.next
                temp.next=self.head.next
            self.head=self.head.next
        else:
            temp=self.head
            pos-=2
            while(pos):
                pos-=1
                temp=temp.next
            temp.next=temp.next.next
    def access(self,pos):
        if self.size()==0:
            return False#Underflow
        if self.size()==1:
            return str(self.head.data)
        temp=self.head
        i=1
        while(True):
            if i==pos:
                return str(temp)
            i+=1
            temp=temp.next
    def copy(self):
        new_list=circular_ll(self.head.data)
        for i in range(2,self.size()+1):
            new_list.insert(self.access(i),i)
        return new_list

if __name__=="__main__":
    l=circular_ll(node(0))
    print(l.size(),l)
    l.insert(1,2)#insert at last
    print(l.size(),l)
    l.insert(-1,1)#insert at beginning
    print(l.size(),l)
    l.insert(99,2)#insert at any pos
    print(l.size(),l)
    l.remove(2)#remove at any pos
    print(l.size(),l)
    c1,c2=l.copy(),l.copy()
    c1.remove(1)#remove first
    c2.remove(c2.size())#remove last
    print(c1.size(),c1)
    print(c2.size(),c2)
    print(l.access(100))#test for circular. If circular 100%3 ie 1st element will be printed
