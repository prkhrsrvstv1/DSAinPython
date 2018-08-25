# This class implements queue using Python list
class Queue(object):

    def __init__(self, head=None):
        self.storage = [head]
    
    # Adds a new_element to the front of the queue
    def enqueue(self, new_element):
        self.storage = [new_element] + self.storage[:]
    
    # Returns the first element from the rear of the queue
    def peek(self):
        return(self.storage[-1])
    
    # Removes and returns the first element from the rear of the queue
    def dequeue(self):
        if len(self.storage) == 0:
            return None
        last_element = self.storage[-1]
        self.storage = self.storage[:-1]
        return(last_element)
