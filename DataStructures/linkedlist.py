import logging

logger = logging.getLogger(__name__)


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value) -> None:
        init_node = Node(value)
        self.head = init_node
        self.tail = init_node
        self.length = 1

    def append(self, value) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True

    def pop(self) -> Node:
        # Edge case 1 : if the LL is empty
        if self.length == 0:
            logger.warning("Empty List encountered, nothing to pop")
            return None
        # Edge case 2 : if the LL had only one item
        elif self.length == 1:
            popped = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            logger.info("Linked list is now empty!")
            return popped
        # LL with some elements
        else:
            pre = self.head
            temp = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            logger.info(temp.value)
            return temp

    def prepend(self, value: int) -> bool:
        node = Node(value)
        # Edge case 1: if the LL is empty
        if self.length == 0:
            self.head = node
            self.tail = node
        # LL with some elements
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return True

    def pop_first(self) -> bool:
        # Edge case 1 :LL is empty

        if self.length == 0:
            logger.warning("LL is empty. nothing to pop")
            return False
        # Edge case 1: LL has only one item, tail also should be modified
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return True
        # LL has some elements
        else:
            temp = self.head
            self.head = temp.next
            self.length -= 1
            print(temp.value)
            return True

    def get_item(self, index: int) -> Node:
        if index < 0 or index > self.length:
            logger.warning("Linked List index is out of range!")
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index: int, value: int) -> bool:
        print(self.length)
        if index < 0 or index > self.length:
            logger.warning("Linked List index is out of range!")
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return True

    def insert(self, index: int, value: int) -> bool:
        if index < 0 or index > self.length:
            logger.warning("Index is nt valid")
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        else:
            node = Node(value)
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            node.next = temp.next
            temp.next = node
            return True
        
    def remove(self, index:int)->Node:
        if index<0 or index >= self.length:
            return None
        if index== 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        ## LL with some elements
        else:
            prev = self.head
            temp = self.head
            for _ in range(index):
                prev = temp
                temp = temp.next

            prev.next = temp.next
            return temp              
    
    def reverse(self)->bool:
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


if __name__ == "__main__":
    my_linked_list = LinkedList(4)
    print(my_linked_list)
    



