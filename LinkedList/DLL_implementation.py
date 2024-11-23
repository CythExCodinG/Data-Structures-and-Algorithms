class node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None
class DoublyLinkedList:
  def __init__(self):
    self.head=None
    self.temp=None
  def addNode(self,data):
    newNode=node(data)

    if(self.head==None):
      self.head=newNode
      self.head.prev=None
      self.temp=newNode
    else:
      newNode.next=None
      newNode.prev=self.temp
      self.temp.next=newNode
      self.temp=self.temp.next
  def display(self):
    ele=self.head

    while ele!=None:
      print("Previous element")
      print(ele.prev)
      print("Next Element")
      print(ele.data)
      ele=ele.next

dList=DoublyLinkedList()
      
dList.addNode(7)
dList.addNode(9)
dList.addNode(8)
dList.addNode(2)

dList.display()