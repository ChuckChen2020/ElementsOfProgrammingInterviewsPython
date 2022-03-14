class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node


def insert_a_list_of_nodes(node, L):
    cur = node
    for val in L:
        cur.next = ListNode(val)
        cur = cur.next


def print_a_linked_list(node):
    cur = node.next
    while cur:
        print(cur.data)
        cur = cur.next


def merge_two_sorted_lists(L1, L2):
    p1, p2 = L1.next, L2.next
    # Thought of keeping the one between L1, L2, whoever has the smaller first value, as the head to return, but it turns out to require tmp     O(n) memory to begin with and is overall rather confusing. The idea of using a new head and keep on hooking its next to the smaller worked better and is more memory-saving.
    head = ListNode()
    cur = head

    while True:
        if p1 == None or p2 == None:
            break
        if p1.data < p2.data:
            cur.next = p1
            p1 = p1.next
        else:
            cur.next = p2
            p2 = p2.next
        cur = cur.next

    cur.next = p1 if p2 == None else p2
    return head


if __name__ == '__main__':
    L1 = ListNode()
    vals_1 = [2, 5, 7]
    L2 = ListNode()
    vals_2 = [3, 11]
    insert_a_list_of_nodes(L1, vals_1)
    # print_a_linked_list(L1)
    insert_a_list_of_nodes(L2, vals_2)
    # print_a_linked_list(L2)
    print_a_linked_list(merge_two_sorted_lists(L1, L2))
