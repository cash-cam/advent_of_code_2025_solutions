import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data, end=' ')
            temp = temp.next
            if temp == self.head:
                break
        print()

# Example Usage
cdll = CircularDoublyLinkedList()
for i in range(0, 100):
        cdll.append(i)



file_path = "input1.txt"
with open(file_path, 'r') as file:
        content = file.read()


number_of_times_through_0 = 0
current_node = cdll.head
for i in range (0, 50):
        current_node = current_node.next

# need to break by \n
for line in content.split("\n"):
        if "R" in line:
                for i in range(int(line[1:])):
                        current_node = current_node.next
                        if current_node.data == cdll.head.data:
                                number_of_times_through_0 = number_of_times_through_0 + 1
                # if current_node.data == cdll.head.data:
                #         number_of_times_through_0 = number_of_times_through_0 + 1
        
                        
        if "L" in line:
                for i in range(int(line[1:])):
                        current_node = current_node.prev
                        if current_node.data == cdll.head.data:
                                number_of_times_through_0 = number_of_times_through_0 + 1
                                   
print(number_of_times_through_0)