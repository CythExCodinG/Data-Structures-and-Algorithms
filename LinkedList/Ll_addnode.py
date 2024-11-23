class node:
  def __init__(self,data):
    self.value=data
    self.next=None

class singlyLinkedList:
  #Intialize node head and tail to none at the start
  def __init__(self):
    self.head=None
    self.tail=None

  #Add new node to linked list 
  def addNode(self,data):
    newNode=node(data)
    
    if(self.head==None):
      self.head=newNode
      self.tail=newNode
    else:
      self.tail.next=newNode
      self.tail=newNode


  
  def addNodeToLast(self,data):

    newNode=node(data)
    self.tail.next=newNode
    self.tail=self.tail.next

  def addToFirst(self,data):
    newNode=node(data)
    newNode.next=self.head
    self.head=newNode
  
  def addToPos(self,data,pos):
    
    newNode=node(data)
    i=0
    temp=self.head
    for i in range(pos+1):
      temp=temp.next

    nxt=temp.next
    temp.next=newNode
    temp=temp.next
    temp.next=nxt

  def addNodeToMiddle(self,data):
    newNode=node(data)
    current=self.head
    count=0
    while(current!=None):
      count=count+1
      current=current.next
    temp=self.head
    i=0
    for i in range(int((count/2)-1)):
      temp=temp.next
    
    nxt=temp.next
    temp.next=newNode
    temp=temp.next
    temp.next=nxt
  

  #Display the linked list  :first check head is empty to check 
  def display(self):
    current=self.head
    if(self.head==None):
      print("list is Empty")
      return
    print("Nodes of singly linked list:")
    while(current!=None):
      print(current.value,end="\n")
      current=current.next

sList=singlyLinkedList()
sList.addNode(6)
sList.addNode(7)
sList.addNode(8)
sList.addNode(20)
sList.addNodeToLast(3)
sList.display()
