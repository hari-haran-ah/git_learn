
# Tree concept

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self,root_value = None):
        if root_value:
            self.root = Node(root_value)
        else:
            self.root = None
    
    def insert_node(self,parent_value,new_node,side):
        if self.root is None:
            print("No will added, first added the root node")
        parent_node = self._find_node(self.root,parent_value)
        
        if parent_node is None:
            print("Parent node not found.")
            return
        if side.lower() == "left":
            new_value = Node(new_node)
            if parent_node.left is None:
                parent_node.left = new_value
            else:
                print("Left child already exists.")
        elif side.lower() == "right":
            new_value = Node(new_node)
            if parent_node.right is None:
                parent_node.right = new_value
            else:
                print("Right child already exists.")
        else:
            print("Side must be 'left' or 'right'.")
        
    def _find_node(self,current_node,value_to_identify):
        if current_node is None:
            return None
        if current_node.value == value_to_identify:
            return current_node
        
        found_node = self._find_node(current_node.left,value_to_identify)
        if found_node:
            return found_node
        return self._find_node(current_node.right,value_to_identify)
    
    
    def display(self):
        if self.root is None:
            print("No Tree ")
        else:
            self._display_helper(self.root,0,"Root:")
    
    def _display_helper(self,node,level,prefix):
        if node:
            print(" " * (level*4) + prefix + str(node.value) )
            
            if node.left is not None or node.right is not None:
                self._display_helper(node.left,level+1,"L--")
                self._display_helper(node.right,level+1,"R--")
                
bt = BinaryTree(10)

bt.insert_node(parent_value=10,new_node=5,side ="left")
bt.insert_node(parent_value=10,new_node=15,side ="right")
bt.insert_node(parent_value=5,new_node=3,side ="left")

bt.display()

# BST
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_node(self.root,value)
        
    def _insert_node(self,current_node,value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_node(current_node.left,value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_node(current_node.right,value)
        
        
    def display(self):
        if self.root is None:
            print("No Tree ")
        else:
            self._display_helper(self.root,0,"Root:")
    
    def _display_helper(self,node,level,prefix):
        if node:
            print(" " * (level*4) + prefix + str(node.value) )
            
            if node.left is not None or node.right is not None:
                self._display_helper(node.left,level+1,"L--")
                self._display_helper(node.right,level+1,"R--")
                
                
    def height(self):
        return self._height_recursive(self.root) 
    def _height_recursive(self,current_node):
        if current_node is None:
            return -1
        left_height = self._height_recursive(current_node.left)
        right_height = self._height_recursive(current_node.right)

        return 1 + max(left_height,right_height)
    
    def balance_tree(self):
        return self._is_balanced_recursive(self.root) != -2
    def _is_balanced_recursive(self,current_node):
        if current_node is None:
            return -1
        left_height = self._is_balanced_recursive(current_node.left)
        if left_height == -2:
            return -2
        right_height = self._is_balanced_recursive(current_node.right)
        if right_height == -2:
            return -2
        if abs(left_height - right_height) >1:
            return -2
        return 1 + max(left_height,right_height)
    def preorder(self):
        result = []
        self._preorder_recursive(self.root,result)
        return result
    def _preorder_recursive(self,node,result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left,result)
            self._preorder_recursive(node.right,result)
    def inorder(self):
        result = []
        self._inorder_recursive(self.root,result)
        return result
    def _inorder_recursive(self,node,result):
        if node:
            self._inorder_recursive(node.left,result)
            result.append(node.value)
            self._inorder_recursive(node.right,result)
    def postorder(self):
        result = []
        self._postorder_recursive(self.root,result)
        return result
    def _postorder_recursive(self,node,result):
        if node:
            self._postorder_recursive(node.left,result)
            self._postorder_recursive(node.right,result)
            result.append(node.value)

# -------------------------------
class CheckBST:
    def is_bst(self, root):
        return self._is_bst_helper(root, float("-inf"), float("inf"))

    def _is_bst_helper(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.value < max_val):
            return False
        return (self._is_bst_helper(node.left, min_val, node.value) and
                self._is_bst_helper(node.right, node.value, max_val))

        
bst = BST()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)


bst.display()
print(f"Height: {bst.height()}")
print(f"Is balanced? {bst.balance_tree()}")

bst.insert(2)
bst.insert(1)

print(f"height:{bst.height()}")
print(f"Is balanced? {bst.balance_tree()}")

print("Inorder Traversal:", bst.inorder())
print("Preorder Traversal:", bst.preorder())
print("Postorder Traversal:", bst.postorder())
checker = CheckBST()
print("Is BST actually BST?", checker.is_bst(bst.root))