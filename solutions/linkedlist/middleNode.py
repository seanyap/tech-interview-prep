# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #list == array / linkedlist == linked with nodes
        
        #easy solution
        #   loop through entire linkedlist and count the number of nodes and
        #   loop linkedlist again half that count to find middle node
        #disadvantage: looping linkedlist 1.5 times, and having to keep track
        #   of linkedlist count and update it whenever adding/deleting node
        
        #"check for 2 edge cases while code below wont work: null head and 
        #linkedlist with only one head" <-- wrong bc the while loop condition
        #can actually work without checking for head and head.next
        # if not head or not head.next:
        #     return head
        
        #"while loop stops one node before the middle"
        #above is somewhat correct and wrong at the same time. i was thinking 
        #   in terms of nodes, however, i should think in terms of edges traveled. 
        #we travel one edge lesser but if we think of the num of edges travel 
        #   instead of num of nodes, ex: if you have 3 nodes, there are only 2 edges 
        #-> if there are even nodes, then there are even-1(odd) num of edges; 
        #-> if there are odd nodes, then there are odd-1(even) edges if you disregard
        #the last node that points to null

        #if you want to find how many edges traveled by fast/nodes traveled except
        #   head, ask "how many edges slow travel, and multiply that by 2"
        #   if slow travel 1 edge, fast travel 2 edges; if slow travels 2 edges, 
        #   fast travels 2x2=4 edges
        #keep in mind: fast is moving "FASTER" than slow. so their gap is ALWAYS
        #   INCREASING. common misconception: at 10km, fast is at 10km, and slow is
        #   NOT at 8km, but 5km
        #notice: in i=2, start to slow ptr takes 2 edges, slow to fast takes another
        #   2 edges; so the middle node splits the linkedlist in half
        # 1 -> 2 -> 3 -> 4 -> 5 -> null (odd length)
        # ^^                            i=0
        #      ^    ^                   i=1
        #           ^         ^         i=2
        # 1 -> 2 -> 3 -> 4 -> null      (even length)
        # ^^                            i=0
        #      ^    ^                   i=1
        #           ^         ^         i=2 
        
        # slow, fast = head, head
        slow = fast = head  #better way
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    