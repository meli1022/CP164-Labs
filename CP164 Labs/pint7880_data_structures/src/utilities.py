"""
------------------------------------------------------------------------
Utilities
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-01-22"
------------------------------------------------------------------------
"""

from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source!= []:
        last_value = source.pop()
        stack.push(last_value)
    return

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not stack.is_empty():
        last_value = stack.pop()
        target.insert(0,last_value)
    return

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    s = Stack()
    
    empty = s.is_empty()
    print(empty)
        
    for i in range(len(source)):
        s.push(source[i])
        peek = s.peek()
        print(peek)
        s.push(source[i])
        pop = s.pop()
        print(pop)
    
    empty = s.is_empty()
    print(empty)
    
    return
        
def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    position = 0 
    while len(source) > 0: 
        p = source.pop(position)
        queue.insert(p)
    return 
        

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while len(queue) != 0: 
        r = queue.remove()
        target.append(r)

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    position = 0 
    while len(source) > 0: 
        p = source.pop(position)
        pq.insert(p)
        
def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while pq.is_empty() == False:
        r = pq.remove()
        target.append(r)
    
    return

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    empty = q.is_empty()
    print("Empty?:{}".format(empty))
    for i in a:
        ins = q.insert(i)
    r = q.remove()
    empty = q.is_empty()
    print('Empty?:{}'.format(empty))
    print('{} was removed'.format(r))
    pe = q.peek()
    print('{} was peeked'.format(pe))


    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    empty = pq.is_empty()
    print("Empty?:{}". format(empty))
    for i in a:
        pq.insert(i)
    r = pq.remove()
    print('{} was removed'.format(r))
    pe = pq.peek()
    print('{} was peeked'.format(pe))


    return

def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist, 
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in source:
        llist._values.append(i)
    for n in range(len(source)):
        source.pop(0)
    return
    
    

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in llist._values:
        target.append(i)
    for n in range(len(llist._values)):
        llist._values.pop(0)
    return


def list_test(a):
    """
    -------------------------------------------------------
    Tests list implementation.
    The methods of List are tested for both empty and 
    non-empty lists using the data in a:
    is_empty, insert, remove, append, index, __contains__,
    find, count, max, min, __getitem__, __setitem__
    Use: list_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    print("Is it empty?: {}".format(lst.is_empty()))
    array_to_list(lst, a)
    lst.insert(0, 5)
    print("Is it empty?: {}".format(lst.is_empty()))
    target = []
    list_to_array(lst, target)
    lst.append(25)
    lst.append(30)
    lst.append(40)
    a = lst.index(25)
    print("Index:{}".format(a))
    b = 25 in lst
    print('Contains:{}'.format(b))
    c = lst.find(25)
    print('Find:{}'.format(c))
    d = lst.count(25)
    print('Count:{}'.format(d))
    e = lst[1]
    print('Getitem:{}'.format(e))
    lst[0] = 6
    print('Setitem:{}'.format(lst[0]))
    lst.remove(6)
    value1 = lst.min()
    value2 = lst.max()
    print('Max:{}'.format(value2))
    print('Min:{}'.format(value1))
    return






