class Element(object):
    
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    
    def print(self):
        if self.head:
            current = self.head
            while True:
                print(current.value, end=' ')
                current = current.next
                if current:
                    print("-->", end=' ')
                else:
                    print("--||")
                    break
        else:
            print("Can't print. List is empty.")


def __main__():
    l = LinkedList()
    l.print()
    e1 = Element(3)
    e2 = Element(99)
    e3 = Element('hey there!')
    e4 = Element('Uncle')
    e5 = Element([3, 2, 6, 4, '3eer4', 2.442])
    l.append(e1)
    l.print()
    l.append(e2)
    l.print()
    l.append(e3)
    l.print()
    l.append(e4)
    l.print()
    l.append(e5)
    l.print()


if __name__ == "__main__":
    __main__()