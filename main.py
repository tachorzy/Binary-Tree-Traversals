#     def printInorder(self):
#         if self.left():
#             self.left.printInorder()
#         print(self.num)
#         if self.right():
#             self.right.printInorder()

#     def printPostorder(self):
#         if self.left():
#             self.left.printPostorder()
#         if self.right():
#             self.right.printPostorder()
#         print(self.num)

#     def printPreorder(self):
#         print(self.num)
#         if self.left():
#             self.left.printPreorder()
#         if self.right():
#             self.right.printPreorder()

#function searches for the root in the given inorder traversal, all values to its right will be right nodes
def search(inorder, root):
    for i in range(len(inorder)):
        if(inorder[i] == root):
            return i

def postorder(n, preorder, inorder):
    root = search(inorder, preorder[0])
    
    if(root != 0): 
        postorder(root, preorder + 1, inorder)
    
    if(root != n-1):
        postorder(n - root - 1, preorder + root + 1, inorder + root + 1)

    return


def main():
    n = int(input())
    preorder = [int(x) for x in input().split()]
    inorder = [int(x) for x in input().split()]

if __name__ == "__main__":
    main()  