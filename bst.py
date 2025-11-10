import node as Node 

# ===========================================================
# AVL CLASS
# ===========================================================
class AVLTree:
    def get_height(self,root):
        if not root:
            return 0
        return root.height
    
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)