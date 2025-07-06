# Classes


class Node:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"Node {self.key}"


class BST:
    def __init__(self):
        self.root = None


# Functions


def inorder_tree_walk(node):
    if node is not None:
        inorder_tree_walk(node.left)
        print(node.key, end=" ")
        inorder_tree_walk(node.right)


def tree_search(node, value):
    if node is None or node.key == value:
        return node
    if value < node.key:
        return tree_search(node.left, value)
    return tree_search(node.right, value)


def tree_minimum(node):
    while node.left is not None:
        node = node.left
    return node


def tree_maximum(node):
    while node.right is not None:
        node = node.right
    return node


def tree_successor(node):
    if node.right is not None:
        return tree_minimum(node.right)
    node_parent = node.parent
    while node_parent is not None and node == node_parent.right:
        node = node_parent
        node_parent = node_parent.parent
    return node_parent


def tree_predecessor(node):
    if node.left is not None:
        return tree_maximum(node.left)
    node_parent = node.parent
    while node_parent is not None and node == node_parent.left:
        node = node_parent
        node_parent = node_parent.parent
    return node_parent


def tree_insertion(bst, node):
    y = None
    x = bst.root

    while x is not None:
        y = x
        if node.key < x.key:
            x = x.left
        else:
            x = x.right

    node.parent = y

    if y is None:
        bst.root = node
    elif node.key < y.key:
        y.left = node
    else:
        y.right = node


def transplant(bst, u, v):
    if u.parent is None:
        bst.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v

    if v is not None:
        v.parent = u.parent


def tree_delete(bst, key):
    node = tree_search(bst.root, key)

    if node.left is None:
        transplant(bst, node, node.right)
    elif node.right is None:
        transplant(bst, node, node.left)
    else:
        y = tree_minimum(node.right)
        if y.parent != node:
            transplant(bst, y, y.right)
            y.right = node.right
            y.right.parent = y
        transplant(bst, node, y)
        y.left = node.left
        y.left.parent = y


# Execution

if __name__ == "__main__":
    # Node creation
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node6 = Node(6)
    node7 = Node(7)
    node9 = Node(9)
    node13 = Node(13)
    node15 = Node(15)
    node17 = Node(17)
    node18 = Node(18)
    node20 = Node(20)

    # Tree construction
    root = node15
    node15.left = node6
    node15.right = node18
    node6.parent = node15
    node6.left = node3
    node6.right = node7
    node18.parent = node15
    node18.left = node17
    node18.right = node20
    node3.parent = node6
    node3.left = node2
    node3.right = node4
    node7.parent = node6
    node7.right = node13
    node17.parent = node18
    node20.parent = node18
    node2.parent = node3
    node4.parent = node3
    node13.parent = node7
    node13.left = node9
    node9.parent = node13

    # Print keys
    inorder_tree_walk(root)

    # Search for keys
    print("\n")
    node = tree_search(root, 3)
    print(node)
    node = tree_search(root, 8)
    print(node)

    # Minimum and maximum keys
    print("\n")
    minimum = tree_minimum(root)
    print(f"Minimum key: {minimum}")
    maximum = tree_maximum(root)
    print(f"Maximum key: {maximum}")

    # Successor and Predecessor
    print("\n")
    successor = tree_successor(node6)
    predecessor = tree_predecessor(node6)
    print(f"The successor of {node6} is {successor}")
    print(f"The predecessor of {node6} is {predecessor}")

    # Tree construction
    print("\n")
    bst = BST()
    tree_insertion(bst, Node(12))
    tree_insertion(bst, Node(5))
    tree_insertion(bst, Node(2))
    tree_insertion(bst, Node(9))
    tree_insertion(bst, Node(18))
    tree_insertion(bst, Node(15))
    tree_insertion(bst, Node(19))
    tree_insertion(bst, Node(13))
    tree_insertion(bst, Node(17))

    inorder_tree_walk(bst.root)

    # Delete a node
    print("\n")
    tree_delete(bst, 18)
    inorder_tree_walk(bst.root)
