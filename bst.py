    import node as Node 

    # ===========================================================
    # AVL CLASS
    # ===========================================================
    class AVLTree:

        def insert(self, root, key):
            if root is None:
                return Node(key)
            if key < root.key:
                root.left = self.insert(root.left, key)
            elif key > root.key:
                root.right = self.insert(root.right, key)
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
        

        def lr_case(self, _1):
            _2 = _1.left
            _3 = _2.right

            _2.right = _3.left #single left
            _3.left = _2
            _1.left = _3.right #single right
            _3.right = _1
            return _3




