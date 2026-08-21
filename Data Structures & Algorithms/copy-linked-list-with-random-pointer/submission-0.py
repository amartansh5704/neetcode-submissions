

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldtocopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldtocopy[curr]
            copy.next = oldtocopy[curr.next]
            copy.random = oldtocopy[curr.random]
            curr = curr.next
        return oldtocopy[head]