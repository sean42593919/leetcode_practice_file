#addTwoNumbers
#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def get_length(node):
        length=0
        while node:
            length+=1
            node=node.next
        return length
    l3=ListNode()
    carry=0
    node=l3
    l1_len=get_length(l1)
    l2_len=get_length(l2)
    for i in range(l1_len if l1_len>l2_len else l2_len):
        l1num=l1.val if l1 else 0
        l2num=l2.val if l2 else 0
        l3num=l1num+l2num+carry
        carry=0
        if l3num>9:
            l3num-=10
            carry=1
        node.next=ListNode(l3num)
        l1=l1.next if l1 else 0
        l2=l2.next if l2 else 0
        node=node.next
    if carry==1:
        node.next=ListNode(1)
    return l3.next