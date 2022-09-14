# node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# list:
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def print(self):
        if self.head is None:
            print("List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insertAt(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def deleteNode(self, key):
        temp = self.head
        if (temp is None):
            return
        if (temp.data == key):
            self.head = temp.next
            temp = None
            return

        while (temp.next.data != key):
            temp = temp.next

        target_node = temp.next
        temp.next = target_node.next
        target_node.next = None


    
