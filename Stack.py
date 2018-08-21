# This class defines an individual element of a stack
class Element(object):
    
    def __init__(self, value):
        self.value = value
        self.next = None


# This class defines a stack and various methods for manipulating it
class Stack(object):

    def __init__(self, top=None):
        self.top = top
    
    # Adds a new element on top of the stack
    def push(self, new_element):
        new_element.next = self.top
        self.top = new_element
        return
    
    # Removes and returns the element at the top of the stack
    def pop(self):
        if self.top == None:
            print("Can't pop. The stack is empty.")
            return
        popped_element = self.top
        self.top = self.top.next
        return popped_element
    
    # Displays the entire stack
    def display(self):
        if self.top == None:
            print("Can't print. The stack is empty.")
            return
        current = self.top
        while current:
            print(current.value)
            current = current.next
        return
