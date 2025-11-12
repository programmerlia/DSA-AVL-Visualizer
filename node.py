class Node:
    def __init__(self,key):
        self.key = key
        # later for movement cases
        self.left = None
        self.right = None
        self.height = 1