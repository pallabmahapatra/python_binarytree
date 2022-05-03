
class Node:
    '''
    each object has three cambers: data, left, right
    '''
    def __init__(self,data,left,right):
        self.data = data
        self.left = left 
        self.right = right
    
    def __repr__(self):
        return f"left: {self.left}, data: {self.data} ,right: {self.right}"

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def create_tree(self,data):
        new_node = Node(data=data,left=None,right=None)

        if self.root == None:
            self.root = new_node
        elif (self.root != None) and (new_node.data < self.root.data):
            cursor = self.root
            while( cursor != None):
                cursor = cursor.left
            cursor = new_node
            
        elif (self.root != None) and (new_node.data > self.root.data):
            cursor = self.root
            while(cursor != None):
                   cursor = cursor.right
            cursor = new_node
            x = None
        else: print("invalid option")

    def inorder_traversal(self):
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
    
    def display(self):
        print(f'left: {self.root.left}, root: {self.root.data}, right: {self.root.right} ')
    



if __name__ == '__main__':

    obj_BTree = BinaryTree()
    # number of nodes
    
    data = [50,40,30]
    for i in data:
        obj_BTree.create_tree(i)
    
    obj_BTree.display()