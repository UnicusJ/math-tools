def binary_convert(num):
    """
    see binary_converter.py
    """
    output = ''
    while num != 0 and num != 1:
        output = str(num%2) + output
        num = num // 2
    output = str(num) + output
    return output


def power_set(s):
    """
    given a set (list) as input, generates the power set (set containing all subsets of original set)
    function removes any duplicates from the original set

    function uses binary representation to generate possible subsets. for example, for 2 elements, we count to 2^2
    in binary:
    00
    01
    10
    11
    which gives us our four permutations. no elements, element 2 only, element 1 only, and both elements
    this generalises to sets of higher cardinality.

    >>> power_set([1,2,3])
    [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

    >>> power_set([])
    [[]]

    >>> power_set(['a'])
    [[], ['a']]

    """

    s_copy = list(set(s))

    power_set_list = []

    # power set has cardinality 2^(original set size)
    for i in range(2**len(s_copy)):
        subset = []
        binary_num = binary_convert(i)
        binary_string = '0'*(len(s_copy)-len(binary_num)) + binary_num

        count = 0

        for val in binary_string[::-1]:
            if val == '1':
                subset.append(s[count])
            count += 1
        power_set_list.append(subset)
    power_set_list = sorted(power_set_list, key = lambda x: len(x))
    return power_set_list




