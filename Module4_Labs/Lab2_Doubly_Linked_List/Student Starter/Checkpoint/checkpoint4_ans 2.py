
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printList(self, node):
        while node != None:
            print(node.data)
            # Get next node
            node = node.next

    def push(self, newData):
        newNode = Node(newData)

        # newNode -> self.head
        newNode.next = self.head

        # If the list is not empty
        if self.head != None:
            self.head.prev = newNode
        # If the list is empty
        else:
            self.head = newNode
            self.tail = newNode

        # The head is now the new node
        self.head = newNode
        self.size += 1

    def pushback(self, newData):
        #Initialize new node
        newNode = Node(newData)

        # If the list is not empty


        if self.head != None:
            temp = self.tail
            temp.next = newNode
            newNode.prev = temp
            self.tail = self.tail.next

        # If the list is empty
        else:
            self.head = newNode
            self.tail = newNode

            # Increment size
        self.size += 1

    def insertAfter(self, target, newData):
        # 1. If the list is empty
        if self.head == None:
            return
        else:
            curr = self.head
            # 2. Search for target node
            while curr.data != target:
                curr = curr.next
        if curr == None:
            print("Target not found.")
            return


        # 3. If target was found, curr != None
        newNode = Node(newData)
        newNode.prev = curr
        newNode.next = curr.next
        # 4. If curr is not the last node
        if curr.next is not None:
            curr.next.prev = newNode

        else:
            self.tail = newNode

            # 5. Connect the current node with the new node
        curr.next = newNode
        # Increment size
        self.size += 1

    def insertBefore(self, target, newData):

        # If the list is empty
        if self.head == None:
            return

        else:
            curr = self.head

            # 2. Search for target node
            while curr.data != target:
                curr = curr.next
                if curr == None:
                    print("Target not found.")
                    return

            # 3. If target was found, curr != None
        newNode = Node(newData)
        newNode.prev = curr.prev
        newNode.next = curr

        # 4. If curr is not the first node
        if curr.prev != None:
            curr.prev.next = newNode

        else:
            self.head = newNode

            # 5. Connect the current node with the new node
        curr.prev = newNode
        # Increment size
        self.size += 1

def main():
    LL = DoublyLinkedList()
    LL.push(1)
    LL.push(2)
    LL.insertAfter(2,3)
    LL.insertAfter(1,4)
    LL.insertBefore(4,9)
    LL.printList(LL.head)

main()