#function searches for the root in the given inorder traversal, all values to its right will be right nodes
def search(inorder, root):
    for i in range(len(inorder)):
        if(inorder[i] == root):
            return i

def postorder(n: int, preorder: list, inorder: list):
    root = search(inorder, preorder[0])
    
    if(root != 0): 
        postorder(root, preorder[1:], inorder)
    
    if(root != n-1):
        postorder(n - root - 1, preorder[root+1:], inorder[root+1:])
    
    print(preorder[0], end=" ")

def main():
    n = int(input())
    preorder = [int(x) for x in input().split()]
    inorder = [int(x) for x in input().split()]

    postorder(n, preorder, inorder)
    
if __name__ == "__main__":
  main()