# The merge two sorted list problem for doubly linked list.
class ListNode:
    def __init__(self, data=0, last_node=None, next_node=None):
        self.data = data
        self.last = last_node
        self.next = next_node


# Search for a key, O(n)
def search_list(L, key):
    while L and L.data != key:
        L = L.next
    return L


# Insert a new node after a specified node
def insert_after(node, new_node):
    if node.next == None:
        node.next = new_node
        new_node.last = node
        return
    tmp = node.next
    node.next = new_node
    new_node.next = tmp
    tmp.last = new_node
    new_node.last = node


# Delete a node
def delete_after(node):
    if node.next.next == None:
        node.next = None
        return
    tmp = node.next.next
    node.next = tmp
    tmp.last = node


def print_a_linked_list(node):
    cur = node.next
    print("Linked List: \nForward pass:")
    while True:
        print(cur.data)
        if cur.next == None:
            break
        cur = cur.next
    print("Backward pass:")
    while True:
        print(cur.data)
        if cur.last == node:
            break
        cur = cur.last


# Doubly linked list version isn't all that different. Only be sure to update links BOTH WAYS!
def merge_two_sorted_lists_dll(L1, L2):
    cur = head = ListNode()
    p1, p2 = L1.next, L2.next
    while True:
        if p1 == None or p2 == None:
            break
        if p1.data < p2.data:
            cur.next = p1
            p1.last = cur
            p1 = p1.next
        else:
            cur.next = p2
            p2.last = cur
            p2 = p2.next
        cur = cur.next
    if p2 == None and p1 != None:
        cur.next = p1
        p1.last = cur
    if p1 == None and p2 != None:
        cur.next = p2
        p2.last = cur

    return head


def insert_a_list_of_nodes(node, L):
    cur = node
    for val in L:
        new_node = ListNode(val)
        cur.next = new_node
        new_node.last = cur
        cur = cur.next


if __name__ == '__main__':
    NodeList = [ListNode(i+1) for i in range(10)]
    head = ListNode(0)
    for idx, node in enumerate(NodeList):
        if idx == 0:
            insert_after(head, NodeList[0])
        else:
            insert_after(NodeList[idx-1], NodeList[idx])
    print_a_linked_list(head)
    insert_after(search_list(head, 7), ListNode(15))
    print_a_linked_list(head)
    delete_after(search_list(head, 7))
    print_a_linked_list(head)
    L1 = ListNode()
    vals_1 = [2, 5, 7]
    L2 = ListNode()
    vals_2 = [3, 11]
    insert_a_list_of_nodes(L1, vals_1)
    print_a_linked_list(L1)
    insert_a_list_of_nodes(L2, vals_2)
    print_a_linked_list(L2)
    print_a_linked_list(merge_two_sorted_lists_dll(L1, L2))
