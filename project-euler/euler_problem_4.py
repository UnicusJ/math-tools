def problem_four():
    max_num = 0
    for x in range(9,91):
        n1 = 11*x
        for y in range(100,1000):
            if is_palindrome(str(y*n1)) and y*n1 > max_num:
                max_num = x*n1
    return max_num


def is_palindrome(string):
    word_list_one = []
    for letter in string:
        word_list_one.append(letter)
    if word_list_one == [word_list_one[x] for x in range(len(word_list_one)-1,-1,-1)]:
        return True
    return False
