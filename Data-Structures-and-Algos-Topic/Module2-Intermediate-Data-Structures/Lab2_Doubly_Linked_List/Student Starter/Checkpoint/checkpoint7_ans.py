def reverse(self): 
    temp = None
    curr = self.head
    self.tail = curr
    
    # Swap next and prev for all nodes of  
    # doubly linked list 
    while curr is not None: 
        temp = curr.prev  
        curr.prev = curr.next
        curr.next = temp 
        curr = curr.prev
        	
        # Before changing head, check for the cases like  
        # empty list and list with only one node 
        if temp is not None: 
            self.head = temp.prev 

def main():
    LL = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('Original List:', LL)
    LL.reverse()
    print('Reversed List:', LL)

main()