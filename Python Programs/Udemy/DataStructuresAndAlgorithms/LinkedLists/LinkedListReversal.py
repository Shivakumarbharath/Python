'''
reverse a linked list



'''

from __init__ import Node

a = Node(1)
b = Node(2)
c = Node(3)

# Linking the nodes
a.nextnode = b
b.nextnode = c

def Reversal(node):

    lst=[]
    while node != None and node.nextnode != None:
        lst.append(node)
        node=node.nextnode
    lst.append(node)
    print(lst)
    lst=lst[::-1]
    for e in range(len(lst)-1):
        lst[e].nextnode=lst[e+1]
    lst[-1].nextnode=None

Reversal(a)
print(c.nextnode.value,b.nextnode.value,a.nextnode)


