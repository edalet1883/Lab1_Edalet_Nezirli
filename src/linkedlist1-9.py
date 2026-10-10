class Node:
    def __init__(self, data):
        self.data = data    
        self.next = None     
class LinkedList:
    def __init__(self):
        self.head = None 

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:       
            self.head = new_node
            return
        current = self.head
        while current.next is not None: 
            current = current.next
        current.next = new_node
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_after(self, target, data):
        current = self.head
        while current is not None:
            if current.data == target:   
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
    def delete(self, value):
        current = self.head
        if current is not None and current.data == value:
            self.head = current.next   
            return
        previous = None
        while current is not None and current.data != value:
            previous = current        
            current = current.next
        if current is not None:      
            previous.next = current.next 
    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                print("Element tapıldı.")
                return
            current = current.next
        print("Element tapılmadı.")
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    def find_max(self):
        max_value = self.head.data
        current = self.head.next
        while current is not None:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value
    def find_min(self):
        min_value = self.head.data
        current = self.head.next
        while current is not None:
            if current.data < min_value:
                min_value = current.data
            current = current.next
        return min_value
    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next     
            current.next = previous  
            previous = current
            current = next_node
        self.head = previous
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
print("n/ Tapşırıq 1 ")
node = Node(15)
print("data =", node.data)
print("next =", node.next)

print("\n Tapşırıq 2")
lst = LinkedList()
for v in (10, 20, 30, 40):
    lst.insert_at_end(v)
lst.display()

print("\n Tapşırıq 3")
lst = LinkedList()
for v in (20, 30, 40):
    lst.insert_at_end(v)
lst.insert_at_beginning(10)
lst.display()

print("\n Tapşırıq 4 ")
lst = LinkedList()
for v in (10, 20, 40):
    lst.insert_at_end(v)
lst.insert_after(20, 30)
lst.display()

print("\n  Tapşırıq 5")
lst = LinkedList()
for v in (10, 20, 30, 40, 50):
    lst.insert_at_end(v)
lst.delete(30)
lst.display()

print("\n Tapşırıq 6")
lst = LinkedList()
for v in (10, 20, 30, 40):
    lst.insert_at_end(v)
lst.search(30)
lst.search(99)

print("\n Tapşırıq 7 ")
lst = LinkedList()
for v in (11, 22, 33, 44, 55):
    lst.insert_at_end(v)
print("List length =", lst.length())

print("\n Tapşırıq 8")
lst = LinkedList()
for v in (23, 8, 91, 15, 42):
    lst.insert_at_end(v)
print("Maximum =", lst.find_max())
print("Minimum =", lst.find_min())

print("\n Tapşırıq 9 ")
lst = LinkedList()
for v in (10, 20, 30, 40, 50):
    lst.insert_at_end(v)
lst.reverse()
lst.display()
