class node:
  def __init__ (self,data):
    self.data = data
    self.next = None

class LL:
  def __init__ (self):
    self.head = None
  
  def print_LL(self):
    if self.head is None:
      print("Linkedlist is empty")
    else:
      n = self.head
      while n is not None:
        print(n.data)
        n= n.next

  def add_begin(self,data):
    new_node = node(data)
    new_node.next = self.head
    self.head = new_node
    
  def add_end(self,data):
    new_node = node(data)
    if self.head is None:
      self.head = new_node
    
    else:
      n = self.head
      while n.next is not None:
        n = n.next
      n.next = new_node
        
LL1 = LL()
LL1.add_begin(10)
LL1.add_begin(12)
LL1.add_begin(32)
LL1.add_end(100)
LL1.print_LL()


