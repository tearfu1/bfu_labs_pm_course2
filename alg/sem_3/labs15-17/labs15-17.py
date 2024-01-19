class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def insert(node, value):
        if node.value is None:
            node.value = value
            return None
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                node.insert(node.left, value)
        elif value >= node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                node.insert(node.right, value)

    @staticmethod
    def search(node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        if value < node.value:
            return node.search(node.left, value)
        else:
            return node.search(node.right, value)

    @staticmethod
    def getMin(node):
        if node is None:
            return None
        if node.left is None:
            return node
        return node.getMin(node.left)

    @staticmethod
    def getMax(node):
        if node is None:
            return None
        if node.right is None:
            return node
        return node.getMax(node.right)

    @staticmethod
    def delete(node, value):
        if node is None:
            return None
        elif value < node.value:
            node.left = node.delete(node.left, value)
        elif value > node.value:
            node.right = node.delete(node.right, value)
        else:
            if node.left is None or node.right is None:
                if node.left is None:
                    node = node.right
                else:
                    node = node.left
            else:
                minRight = node.getMin(node.right)
                node.value = minRight.value
                node.right = node.delete(node.right, minRight.value)

        return node

    @staticmethod
    def inorderTraversal(node):
        if node is None:
            return None
        node.inorderTraversal(node.left)
        print(node.value, end=" ")
        node.inorderTraversal(node.right)

    @staticmethod
    def preorderTraversal(node):
        if node is None:
            return None
        print(node.value, end=" ")
        node.preorderTraversal(node.left)
        node.preorderTraversal(node.right)

    @staticmethod
    def postorderTraversal(node):
        if node is None:
            return None
        node.postorderTraversal(node.left)
        node.postorderTraversal(node.right)
        print(node.value, end=" ")

    @staticmethod
    def stackPreorderTraversal(node):
        stack = LinkedStack()
        while (not (node is None)) or (not stack.is_empty()):
            if not stack.is_empty():
                node = stack.pop()
            while not(node is None):
                print(node.value, end=" ")
                if not (node.right is None):
                    stack.push(node.right)
                node = node.left

    def setWithLine(self, line):
        notNumbers = "(), "
        end = 0
        tempLine = line
        while len(tempLine):
            if tempLine[end] in notNumbers:
                num = tempLine[:end]
                if num != "":
                    self.insert(self, int(num))
                tempLine = tempLine[end+1:]
                end = 0
            else:
                end += 1

    @staticmethod
    def printWithLine(node):
        if node is None:
            return None
        print(node.value, end="")
        if not (node.left is None) or not(node.right is None):
            print(" (", end="")
        node.printWithLine(node.left)
        if not (node.left is None) or not(node.right is None):
            print(", ", end="")
        node.printWithLine(node.right)
        if not (node.left is None) or not(node.right is None):
            print(")", end="")


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.right = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        item = self.top.value
        self.top = self.top.right
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value


print("input a binary tree: ")
newline = input()

Tree = Node()
Tree.setWithLine(newline)
while True:
    print("\nWhat do you want to do with tree?")
    print("1) insert")
    print("2) delete")
    print("3) search")
    print("4) print preorder")
    print("5) print inorder")
    print("6) print postorder")
    print("7) print with linear bracket view")
    print("8) print stack preorder")
    print("0) exit")
    event = int(input())
    match event:
        case 1:
            print("input a number to insert")
            num = int(input())
            Node.insert(Tree, num)
        case 2:
            print("input a number to delete")
            num = int(input())
            Node.delete(Tree, num)
        case 3:
            print("input a number to search")
            num = int(input())
            temp = Node.search(Tree, num)
            Node.printWithLine(temp)
        case 4:
            Node.preorderTraversal(Tree)
        case 5:
            Node.inorderTraversal(Tree)
        case 6:
            Node.postorderTraversal(Tree)
        case 7:
            Node.printWithLine(Tree)
        case 8:
            Node.stackPreorderTraversal(Tree)
        case 0:
            break

Node.printWithLine(Tree)
