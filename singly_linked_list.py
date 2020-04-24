class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return str(self.data)


class singly_ll:
    def __init__(self,data=None):
        self.head=data if type(data) == type(node()) else node(data)
        if data is None:
            self.head = None

    def size(self):
        temp,size=self.head,0
        while(temp is not None):
            size+=1
            temp=temp.next
        return size
    def insert(self,data,pos=1):
        noob=data if type(data) == type(node()) else node(data)
        if pos==1 or self.head is None:
            noob.next=self.head
            self.head=noob
        else:
            pos-=2
            temp=self.head
            while(pos):
                temp=temp.next
                pos-=1
            noob.next=temp.next
            temp.next=noob
    def __str__(self):
        temp=self.head
        out=""
        while temp is not None:
            out+=str(temp)+"->"
            temp=temp.next
        out+="NULL"
        return out
    def remove(self,pos):
        if pos==1:
            self.head=self.head.next
        else:
            temp=self.head
            pos-=2
            while(pos):
                pos-=1
                temp=temp.next
            temp.next=temp.next.next
    def access(self,pos):
        temp=self.head
        i=1
        while(temp is not None):
            if i==pos:
                return str(temp)
            i+=1
            temp=temp.next
        return False#Underflow
    def copy(self):
        new_list=singly_ll(self.head.data)
        for i in range(2,self.size()+1):
            new_list.insert(self.access(i),i)
        return new_list

if __name__=="__main__":
    l=singly_ll(node(0))
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
