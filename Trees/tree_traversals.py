from binarytree import build

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = None
    self.right = None
  
class Tree:
  def __init__(self, TreeNode=TreeNode()):
    self.root = TreeNode
  
  def plot():
    pass

def getTree(nodes):
  node = TreeNode()
  root = node

  queue = []
  node.val = nodes[0]
  queue.append((node, 0))

  offset = 0
  while queue:
    n, idx = queue.pop(0)
    left_index = offset + idx + 1
    right_index = offset + idx + 2

    if left_index >= len(nodes) - 1:
      continue

    left_val = nodes[left_index]
    right_val = nodes[right_index]

    n.left = TreeNode(left_val)
    n.right = TreeNode(right_val)

    queue.append((n.left, left_index))
    queue.append((n.right, right_index))
    offset += 1
  return root

def getTree2(nodes):
  node = TreeNode()
  root = node

  queue = []
  node.val = nodes[0]
  queue.append((node, 0))

  offset = 0
  while queue:
    n, idx = queue.pop(0)
    left_index = offset + idx + 1
    right_index = offset + idx + 2

    if left_index >= len(nodes) - 1:
      continue

    left_val = nodes[left_index]
    right_val = nodes[right_index]

    n.left = TreeNode(left_val)
    n.right = TreeNode(right_val)

    queue.append((n.left, left_index))
    queue.append((n.right, right_index))
    offset += 1
  return root


nodes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,None]
root = getTree(nodes)

root_from_list = build(nodes)
print(root_from_list)

preorder = []

def preorder_traversal(node):
  if node is None:
    return
  preorder.append(node.val)
  preorder_traversal(node.left)
  preorder_traversal(node.right)

preorder_traversal(root)
print("Preorder Traversal:", preorder)

inorder = []

def inorder_traversal(node):
  if node is None:
    return
  inorder_traversal(node.left)
  inorder.append(node.val)
  inorder_traversal(node.right)
  
inorder_traversal(root)
print("Inorder Traversal:", inorder)
# print("Preorder Traversal:", order)
