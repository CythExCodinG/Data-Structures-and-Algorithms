class Node:
  def __init__(self,data):
    self.value=data
    self.next=None

class SinglyLinkedList:
  def __init__(self):
    self.head=None

  def addNodeToBegin(self):
    data=int(input("Enter a data value :"))
    newNode=Node(data)

    if self.head==None:
      self.head=newNode
    else:
      newNode.next=self.head
      self.head=newNode

  def display(self):
    temp=self.head
    while(temp!=None):
      print(temp.value)
      temp=temp.next

LList=SinglyLinkedList()
choice=0
choice=int(input("Enter a Data"))
while(choice==1):
  LList.addNodeToBegin()
LList.display()
# LList.addNodeToBegin(5)
# LList.addNodeToBegin(8)
# LList.addNodeToBegin(2)
# LList.addNodeToBegin(9)
# LList.addNodeToBegin(2)
