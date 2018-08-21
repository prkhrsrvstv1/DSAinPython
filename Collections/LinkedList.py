# This class defines an individual element of the linked list
class Element(object):
    
    def __init__(self, value):
        self.value = value
        self.next = None

# This class defines a linked list and various methods for manipulating it
class LinkedList(object):
    
    def __init__(self, head=None):
        self.head = head
    
    # Adds a new_element to the end of the list
    def append(self, new_element):
        if self.head == None:
            self.head = new_element
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_element
        return
    
    # Inserts the new_element at index(th) position in the list
    def insert(self, new_element, index):
        if index == 1:
            new_element.next = self.head
            self.head = new_element
            return
        if self.head == None:
            print("ERROR: Can't insert at index:" + str(index) + ". List is empty.")
            return
        current = self.head
        counter = 1
        while current and counter < index-1:
            current = current.next
            counter += 1
        if not current:
            print("Insert unsuccesful. Index out of bounds.")
            return
        new_element.next = current.next
        current.next = new_element
        return
    
    # Deletes the element at the index(th) position
    def delete(self, index):
        if not self.head:
            print("Can't delete. List is empty.")
            return
        if index == 1:
            self.head = self.head.next
            return
        current = self.head
        counter = 1
        while current and counter < index-1:
            current = current.next
            counter += 1
        if not current or not current.next:
            print("Delete unsuccessful. Ran out of bounds.")
            return
        current.next = current.next.next

    # Deletes an element from the end of the list and returns it
    def pop(self):
        if not self.head:
            print("Can't pop. List is empty.")
            return
        current = self.head
        if current.next == None:
            popped_element = current
            self.head = None
            return popped_element
        while current.next.next:
            current = current.next
        popped_element = current.next
        current.next = None
        return popped_element
    
    # Prints the entire list
    def display(self):
        if not self.head:
            print("Can't display. List is empty.")
            return
        current = self.head
        while current:
            print(current.value, end='')
            current = current.next
            if current:
                print("-->", end='')
            else:
                print()
        return
