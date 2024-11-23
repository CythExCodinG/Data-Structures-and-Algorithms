class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
  
class Stack:
  def __init__(self):
    self.top=None
  
  def push(self,data):
    newNode=Node(data)
    if self.top==None:
      self.top=newNode
    else:
      newNode.next=self.top
      self.top=newNode

  def pop(self):
    print("Popped Element is :",self.top.data)
    self.top=self.top.next

  def display(self):
    print(self.top.data," <---- TOP")
    temp=self.top
    temp=temp.next
    while(temp!=None):
      print(temp.data)
      temp=temp.next

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.display()
stack.pop()
stack.display()