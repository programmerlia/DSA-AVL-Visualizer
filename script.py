import tkinter as tk
from node import Node
from bst import AVLTree

# ===========================================================
# AVL VISUALIZER USING TKINTER
# ===========================================================
class BSTVisualizer:
    def __init__(self, window):
        self.window = window
        self.window.title("Binary Search Tree Visualizer")
        self.window.geometry("1000x600")
        self.window.configure(bg="white")

        self.tree = AVLTree()
        self.root = None

        # Entry widget for input
        self.entry = tk.Entry(self.window, width=15, font=('Arial', 14))
        self.entry.pack(pady=10)

        # Insert button
        self.insert_button = tk.Button(
            self.window, text="Insert", command=self.insert_value,
            font=('Arial', 12), bg="#4CAF50", fg="black"
        )
        self.insert_button.pack(pady=5)
        #Deletion button
        self.clear_button = tk.Button(
            self.window, text="Clear Tree", command=self.clear_tree,
            font=('Arial', 12), bg="#f44336", fg="white"
        )
        self.clear_button.pack(pady=5)

        # Canvas for drawing the tree
        self.canvas = tk.Canvas(self.window, width=980, height=500, bg="white", highlightthickness=1, highlightbackground="gray")
        self.canvas.pack(pady=10)

        # Label for messages
        self.status = tk.Label(self.window, text="Enter a number and click Insert", font=('Arial', 12), bg="white")
        self.status.pack()

    # Function to handle inserting values
    def insert_value(self):
        value = self.entry.get().strip()

        # Validate input
        if not value.lstrip('-').isdigit():
            self.status.config(text="Please enter a valid integer.", fg="red")
            return

        key = int(value)
        self.root = self.tree.insert(self.root, key)
        self.entry.delete(0, tk.END)
        self.status.config(text=f"Inserted {key} into the BST.", fg="green")

        #insert function herreeeeeee---------------

        # Redraw tree after insertion
        self.redraw_tree()

    # Recursive function to draw the tree
    def draw_tree(self, node, x, y, x_offset):
        if node is not None:
            # Draw left child and connecting line
            if node.left:
                self.canvas.create_line(x, y, x - x_offset, y + 60, fill="gray", width=2)
                self.draw_tree(node.left, x - x_offset, y + 60, x_offset / 2)

            # Draw right child and connecting line
            if node.right:
                self.canvas.create_line(x, y, x + x_offset, y + 60, fill="gray", width=2)
                self.draw_tree(node.right, x + x_offset, y + 60, x_offset / 2)

            # Draw node (circle)
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="#4CAF50", outline="black", width=2)
            self.canvas.create_text(x, y, text=str(node.key), fill="white", font=('Arial', 12, 'bold'))

    # Function to refresh the canvas
    def redraw_tree(self):
        self.canvas.delete("all")
        if self.root:
            self.draw_tree(self.root, 500, 50, 250)
        else:
            self.status.config(text="Tree is empty.", fg="black")

    def clear_tree(self):
        self.root = None
        self.redraw_tree()
        self.status.config(text="Tree cleared.", fg="blue")


# ===========================================================
# MAIN PROGRAM
# ===========================================================
if __name__ == "__main__":
    window = tk.Tk()
    app = BSTVisualizer(window)
    window.mainloop()