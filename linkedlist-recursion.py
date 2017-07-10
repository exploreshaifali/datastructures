def travel_linkedlist(curr):
    """Recursively travel to linkedlist."""
    if curr is None:
        return
    print(curr.data)
    travel_linkedlist(curr._next)


def travel_space_separated(curr):
    """Print space separated linked list elements."""
    if curr is None:
        return ""
    print(curr.data, end=' ')
    travel_space_separated(curr._next)


def travel_reverse(curr):
    """Print elemets in linked-list in reverse order."""
    if curr is None:
        return
    travel_reverse(curr._next)
    print(curr.data, end=' ')
