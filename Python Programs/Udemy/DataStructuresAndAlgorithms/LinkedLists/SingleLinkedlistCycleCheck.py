'''

Given single linked list
check whether the list is looped or not



'''

class Node:
    def __init__(self, value):
        self.value = value  # to store the value
        self.nextnode = None  # to store the reference of the next node



a = Node(1)
b = Node(2)
c = Node(3)

# Linking the nodes
a.nextnode = b
b.nextnode = c
#c.nextnode=a

def cycle_check(a):
    global s

    s=[]
    def check(a):


        if a in s:
            return True

        if a.nextnode!=None:

            s.append(a)
            return check(a.nextnode)

        else:
            return False

    return  check(a)

print(cycle_check(a))

'''
Different analogy

We will have two markers traversing the list 
marker1 and marker 2
Both will begin at the first node and
marker one will traveersr one node at the time and marker 2 will traverse two nodes at a time 

By this logic we can imagine the markers are racing through the linked list 
with the marker two moving fast 
if linked list is a cycle at one point of time 
marker 1 will be equal to marker two

If they are not in cycle marker 2 will reach None 


'''
def cycle_check2(node):
    marker1=node
    marker2=node

    while marker2!=None and marker2.nextnode!=None:
        # marker2.nextnode!=None:  if this is not given  marker2=marker2.nextnode.nextnode rises an error
        marker1=marker1.nextnode
        marker2=marker2.nextnode.nextnode

        if marker1==marker2:
            return True

    return False


print(cycle_check2(a))