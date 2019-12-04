def int_to_char(num_list):
    """
    converts a list of numbers to a list of letters, using the standard num/letter conversion:
    A--> 0, B--> 1, ... Z--> 25
    """
    letter_list = []
    for num in num_list:
        letter_list.append(chr(num+65))
    return letter_list


def char_to_int(word):
    """
    takes a string as input, and converts it to a list of numbers using standard conversion:
    A--> 0, B--> 1, ... Z--> 25
    """
    word = word.upper()
    num_list = []
    for letter in word:
        num_list.append(ord(letter)-65)
    return num_list


def caesar_cipher(P,k):
    """
    takes a plaintext in the form of a string, and an encryption key, k
    function converts plaintext to nums, applies the encryption by adding the key modulo 26, and converting back to
    text, giving us our ciphertext.

    to decrypt, you can use the same function, use k = -1 * (encryption key)

    >>> caesar_cipher('HELLO', 3)
    'KHOOR'

    >>> caesar_cipher('KHOOR', -3)
    'HELLO'

    """
    nums = char_to_int(P)
    C = []
    for num in nums:
        C.append((num+k)%26)
    C = int_to_char(C)
    return ''.join(C)


