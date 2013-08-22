class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.value

    def printNode(self):
        print self.value
        if self.next:
            self.next.printNode()

    def reverse( self ):
        # Find the head
        head = self
        while ( head.prev ):
            head = head.prev

        node = head
        prev = None

        while ( node ):
            temp = node.next
            node.next = node.prev
            node.prev = temp

            # The old next, the new previous will be the next node we process.
            prev = node
            node = node.prev

        return prev  # The new head


def main(argv):
    s = "this is a really awesome"
    # print argv
    arr = s.split()
    l = ll(arr)
    #print l
    l.printNode()
    r = l.reverse()
    r.printNode()


def ll( argv ):
    prev = None
    head = None
    for arg in argv:
        node = Node(arg, None, prev)
        if prev is None:
            head = node
        else:
            prev.next = node
        prev = node
    return head


main("something")