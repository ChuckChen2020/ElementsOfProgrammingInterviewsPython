class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


# Search for a key, O(n)
def search_list(L, key):
    while L and L.data != key:
        L = L.next
    return L


# Insert a new node after a specified node
def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node


# Delete a node
def delete_after(node):
    node.next = node.next.next


if __name__ == '__main__':
    NodeList = [ListNode(i+1) for i in range(10)]
    head = ListNode(0)
    for idx, node in enumerate(NodeList):
        if idx == 0:
            insert_after(head, NodeList[0])
        else:
            insert_after(NodeList[idx-1], NodeList[idx])
    print(search_list(head, 7).data, search_list(head, 7).next.data)
    insert_after(search_list(head, 7), ListNode(15))
    print(search_list(head, 15).next.data)
    delete_after(search_list(head, 7))
    print(search_list(head, 7).next.data)
