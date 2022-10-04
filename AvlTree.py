# Author         : Malay Jeena
# Python3 concept: Avl Tree insertion and deletion
# GITHUB         : https://github.com/Malay998

# queue concept
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def IsEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def enqueue(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.IsEmpty():
            return 'Queue is Empty!'

        else:
            temp = self.head
            self.head = temp.next
            return temp.value

# levelorder
def levelorder(rootnode):
    if not rootnode:
        return 'Tree does not exist'

    q = Queue()
    q.enqueue(rootnode)

    while not q.IsEmpty():
        root = q.dequeue()
        print(root.data)

        if root.leftchild is not None:
            q.enqueue(root.leftchild)

        if root.rightchild is not None:
            q.enqueue(root.rightchild)


# AvlTree concept

class AvlNode():
    def __init__(self, data=None):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1


def getHeight(rootnode):
    '''
    Function to get the height of the rootnode

    '''
    if not rootnode:
        return 0
    return rootnode.height


def rotateRight(disbalance_node):
    '''
    Function for the right rotation in the avl tree
    '''
    new_root = disbalance_node.leftchild

    disbalance_node.leftchild = disbalance_node.leftchild.rightchild

    new_root.rightchild = disbalance_node

    # setting the height for disbalance_node and  new_root

    disbalance_node.height = 1 + max(getHeight(disbalance_node.leftchild), getHeight(disbalance_node.rightchild))

    new_root.height = 1 + max(getHeight(new_root.leftchild), getHeight(new_root.rightchild))

    return new_root


def rotateLeft(disbalance_node):
    '''
    Function for the left rotation in the avl tree
    '''
    new_root = disbalance_node.rightchild

    disbalance_node.rightchild = disbalance_node.rightchild.leftchild

    new_root.leftchild = disbalance_node

    # Setting the height

    disbalance_node.height = 1 + max(getHeight(disbalance_node.leftchild), getHeight(disbalance_node.rightchild))

    new_root.height = new_root.height = 1 + max(getHeight(new_root.leftchild), getHeight(new_root.rightchild))

    return new_root


def getBalance(rootnode):
    '''
    Function to check if the tree is balance
    '''

    return getHeight(rootnode.leftchild) - getHeight(rootnode.rightchild)


def insert(rootnode, nodevalue):
    if not rootnode:
        return AvlNode(nodevalue)

    elif nodevalue < rootnode.data:
        rootnode.leftchild = insert(rootnode.leftchild, nodevalue)

    else:
        rootnode.rightchild = insert(rootnode.rightchild, nodevalue)

    rootnode.height = 1 + max(getHeight(rootnode.leftchild), getHeight(rootnode.rightchild))
    balance = getBalance(rootnode)
    #print(f"h of {rootnode.data} = {rootnode.height} and balance = {balance}")

    if (balance > 1 and nodevalue < rootnode.leftchild.data):
        # rootnode --> leftchild --> leftchild (nodevalue)
        # Left left condition
        return rotateRight(rootnode)

    if (balance > 1 and nodevalue > rootnode.leftchild.data):
        # Left right condition
        # rootnode --> leftchild --> rightchild (nodevalue)
        # doing left rotation in the left child of the rootnode

        rootnode.leftchild = rotateLeft(rootnode.leftchild)
        return rotateRight(rootnode)

    if (balance < -1 and nodevalue > rootnode.rightchild.data):
        # rootnode --> rightchild --> rightchild(nodevalue)
        # Right right condition

        return rotateLeft(rootnode)

    if (balance < -1 and nodevalue < rootnode.rightchild.data):
        # Right Left condition
        # rootnode --> rightchild --> leftchild (nodevalue)

        rootnode.rightchild = rotateRight(rootnode.rightchild)
        return rotateLeft(rootnode)

    return rootnode


# Deletion of AVL Node

def minValue(rootnode):
    '''

    :param rootnode:
    :return: mininmum value of the rightchild of the rootnode
    '''
    temp = rootnode
    while temp.leftchild is not None:
        temp = temp.leftchild
    return temp


def deleteAvlNode(rootnode, nodevalue):
    if not rootnode:
        return "Rootnode does not exist!!"


    elif nodevalue < rootnode.data:
        rootnode.leftchild = deleteAvlNode(rootnode.leftchild, nodevalue)

    elif nodevalue > rootnode.data:
        rootnode.rightchild = deleteAvlNode(rootnode.rightchild, nodevalue)

    else:

        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode = None
            return temp

        elif rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp

        minvalue = minValue(rootnode.rightchild)
        rootnode.data = minvalue.data
        rootnode.rightchild = deleteAvlNode(rootnode.rightchild, minvalue.data)

        balance = getBalance(rootnode)

        if balance > 1 and getBalance(rootnode.leftchild) >= 0:
            return rotateRight(rootnode)

        if balance > 1 and getBalance(rootnode.leftchild) < 0:
            rootnode.leftchild = rotateLeft(rootnode.leftchild)
            return rotateRight(rootnode)

        if balance < -1 and getBalance(rootnode.rightchild) <= 0:
            return rotateLeft(rootnode)

        if balance < -1 and getBalance(rootnode.rightchild) > 0:
            rootnode.rightchild = rotateRight(rootnode.rightchild)
            return rotateLeft(rootnode)

    return rootnode


if __name__ == '__main__':
    new_avl = AvlNode(30)
    new_avl = insert(new_avl, 25)
    new_avl = insert(new_avl, 20)
    new_avl = insert(new_avl, 15)
    new_avl = insert(new_avl, 5)
    new_avl = insert(new_avl, 10)
    new_avl = insert(new_avl, 50)
    new_avl = insert(new_avl, 60)
    new_avl = insert(new_avl, 70)
    new_avl = insert(new_avl, 25)
    new_avl = insert(new_avl, 65)

    # levelorder
    print(levelorder(new_avl))
    print("***********************")

    # deletion
    deleteAvlNode(new_avl, 70)
    deleteAvlNode(new_avl, 30)
    deleteAvlNode(new_avl, 50)

    # levelorder
    print(levelorder(new_avl))
