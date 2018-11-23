"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: Node) -> str:
    if root is None:
        return ""

    queue = list([root])
    result = ""
    while queue:
        current = queue.pop(0)
        if current is None:
            result += "0"
        else:
            result += str(len(current.val)) + str(current.val)
            queue.append(current.left)
            queue.append(current.right)
    return result

def deserialize(string: str) -> Node:
    if not string:
        return None

    arr = list()

    from_idx = 0
    to_idx = 1

    while from_idx < len(string):
        length = int(string[from_idx:to_idx])
        if length == 0:
            from_idx += 1
            to_idx += 1
            arr.append(None)
        else:
            from_idx += 1
            to_idx += length
            arr.append(string[from_idx:to_idx])
            from_idx = to_idx
            to_idx += 1
    if not arr:
        return None


    for i in range(len(arr)):
        node = Node(arr[i])
        if (2*i + 2 > len(arr)):
            break
        left = 2*i + 1
        right = left + 1
        parent = int(i / 2)

        if parent * 2 + 1 == i and i != 0:
            arr[parent].left = node
        elif parent * 2 + 2 == i and i != 0:
            arr[parent].right = node

        if arr[left] == None:
            node.left = None
        else:
            node.left = Node(arr[left])

        if arr[right] == None:
            node.right = None
        else:
            node.right = Node(arr[right])

        arr[i] = node
    return arr[0]

node = Node('root', Node('left', Node('left.left')), Node('right'))

print(deserialize(serialize(node)).left.left.val)
