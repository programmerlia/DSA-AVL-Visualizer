from node import Node
# ===========================================================
# AVL CLASS
# ===========================================================
class AVLTree:

    def insert(self, root, key):
        if root is None:
            return Node(key)
        
        #inserts 
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        #Get balance
        balance = self.get_balance(root)


        # LL Case
        if balance > 1 and key < root.left.key:
            return self.ll_case(root)  

        # RR Case
        if balance < -1 and key > root.right.key:
            return self.rr_case(root) 

        # LR Case
        if balance > 1 and key > root.left.key:
            root.left = self.rr_case(root.left) 
            return self.ll_case(root)  

        # RL Case
        if balance < -1 and key < root.right.key:
            root.right = self.ll_case(root.right) 
            return self.rr_case(root) 

        return root

    def get_height(self,root):
        if not root:
            return 0
        return root.height
    
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    #rotations
    def ll_case(self, _1):
        _2 = _1.left
        child = _2.right
        _2.right = _1
        _1.left = child

        _2.height = 1+max(self.get_height(_2.left), self.get_height(_2.right))
        _1.height = 1+max(self.get_height(_1.left), self.get_height(_1.right))
        
        return _2
    
    def rr_case(self, _1):
        _2 = _1.right
        child = _2.left
        _2.left = _1
        _1.right = child

        _2.height = 1+max(self.get_height(_2.left), self.get_height(_2.right))
        _1.height = 1+max(self.get_height(_1.left), self.get_height(_1.right))
        return _2
    