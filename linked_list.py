class node():
    def __init__(self,data):
        self.data = data;
        self.next = None;
    def set_next(self, node):
        self.next = node;
        

n1 = node(6)
head = n1;
n2 = node(4);
n1.set_next(n2)
n3 = node(2)
n2.set_next(n3)
n4 = node(0)
n3.set_next(n4)

n = head
while(1):
    print(n.data)
    if(n.next==None):
        break;
    n = n.next
