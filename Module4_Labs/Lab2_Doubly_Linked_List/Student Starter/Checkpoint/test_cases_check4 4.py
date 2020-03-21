"""
Test Case 1
def main():
    LL = DoublyLinkedList()
    LL.push(1)
    LL.push(2)
    LL.push(3)
    LL.push(5)
    LL.push(9)
    LL.printList(LL.head)
"""
"""
Test Case 1 - Results
9
5
3
2
1
"""

"""
Test Case 2
def main():
    LL = DoublyLinkedList()
    LL.push(1)
    LL.push(2)
    LL.push(3)
    LL.pushback(5)
    LL.pushback(9)
    LL.printList(LL.head)
"""

"""
Test Case 2 - Results
3
2
1
5
9
"""


"""
Test Case 3
def main():
    LL = DoublyLinkedList()
    LL.push(1)
    LL.push(2)
    LL.push(3)
    LL.pushback(5)
    LL.insertAfter(5,10)
    LL.pushback(9)
    LL.insertAfter(9,11)
    LL.insertAfter(10,12)
    LL.insertAfter(3,4)
    LL.insertAfter(11,14)
    LL.printList(LL.head)
"""

"""
Test Case 3 - Results
3
4
2
1
5
10
12
9
11
14
"""

"""
Test Case 4
def main():
    LL = DoublyLinkedList()
    LL.push(1)
    LL.push(2)
    LL.push(3)
    LL.insertBefore(3,4)
    LL.insertBefore(4,5)
    LL.insertBefore(4,4.5)
    LL.insertBefore(1,10)
    LL.printList(LL.head)
"""

"""
Test Case 4 - Results
5
4.5
4
3
2
10
1
"""

