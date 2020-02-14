#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length  # [None, None, None]

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    for i in range(length):
        if route[i - 1] is not None:
            route[i] = hash_table_retrieve(hashtable, route[i - 1])
        else:
            route[i] = hash_table_retrieve(hashtable, "NONE")
    return route[:-1]
