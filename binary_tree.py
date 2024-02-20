class Node:
    '''
    each object has three chambers: data, left, right
    '''
    def __init__(self,data,left,right):
        self.data = data
        self.left = left 
        self.right = right
    
    # def __repr__(self):
    #     return f"left: {self.left}, data: {self.data} ,right: {self.right}"

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def create_tree(self,data):
        new_node = Node(data=data,left=None,right=None)

        if self.root == None:
            self.root = new_node
        
        # data that are less than root
        elif new_node.data < self.root.data:
            cursor = self.root
            #cursor.left = new_node
            while(cursor.left):
                cursor = cursor.left
            cursor.left = new_node
        
        elif new_node.data > self.root.data:
            cursor = self.root
            #cursor.right = new_node
            while(cursor.right):
                cursor = cursor.right
            cursor.right = new_node
        else:
            print("invalid  condition")
        
        
    def inorder_traversal(self):
        print("inorder traversal:\n")
        cursor = self.root
        flag = True
        stack = []
        while(flag):
            if cursor:
                stack.append(cursor)
                cursor = cursor.left
            else:
                if stack:
                    cursor = stack.pop()
                    print(cursor.data)
                    cursor = cursor.right
                else: 
                    flag = False

    def preorder_traversal(self):
        print(f'preorder traversal ....\n')
        if self.root:
            current = self.root
            temp_stack = []
            temp_stack.append(current)
            while(current):
                data = 
                print(current.data)


        x = None

if __name__ == '__main__':

    obj_BTree = BinaryTree()
    # number of nodes
    
    data = [50,40,70]
    for i in data:
        obj_BTree.create_tree(i)
    
    #obj_BTree.display()
    obj_BTree.preorder_traversal()