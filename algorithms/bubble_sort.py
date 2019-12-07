def bubble_sort(unsorted_list):
    """
    uses bubble sort algorithm to sort a list of integers or strings
    takes an unsorted list as input, and returns a new list, without changing the original one
    
    >>> bubble_sort([1,3,2])
    [1, 2, 3]

    >>> bubble_sort(['dog', 'cat', 'donkey'])
    ['cat', 'dog', 'donkey']

    >>> bubble_sort([])
    []

    """

    sorted_list = [x for x in unsorted_list]
    for x in range(len(sorted_list)):
        for y in range(len(sorted_list)-x):
            try:
                if sorted_list[y] > sorted_list[y+1]:
                    sorted_list[y], sorted_list[y+1] = sorted_list[y+1], sorted_list[y]
            except IndexError:
                pass

    return sorted_list








