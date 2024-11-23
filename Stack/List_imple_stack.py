stack=[]
top=None

def is_empty(s):
  if len(s)==0:
    return True
  else:
    return False

def push(s):
  val=int(input("Enter element to ppush :"))
  s.append(val)
  display(s)


def pop(s):
  if is_empty(s):
    print(" List is Empty ")
  else:
    top=len(s)-1
    print("Element removed is :",s[top])
    del s[top]
  display(s)
  

def display(s):
  top=len(s)-1
  print(s[top],"<---- Top")
  top=top-1
  while(top>=0):
    print(s[top])
    top=top-1


push(stack)
push(stack)
push(stack)
push(stack)
push(stack)
push(stack)
pop(stack)
