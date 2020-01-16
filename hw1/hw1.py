def funky_sum(a, b, mix):
    """
    Returns a mixture between a and b.

    If mix is 0, returns a. If mix is 1, returns b. Otherwise returns a linear
    interpolation between them. If mix is outside the range of 0 and 1, it is
    capped at those numbers.
    """
    if mix < 0:
        return a
    elif mix > 1:
        return b
    else:
        return (1 - mix) * a + mix * b


def count_divisible_digits(n, m):
    """
    Takes two integers n and m, and returns the number of digits in n that
    are divisible by m.
    """

    # Edge cases
    if m == 0:
        # Can't divide by m, spec states this should be 0
        return 0

    if n == 0:
        # Can't loop through n, 0 is divisible by all m
        return 1

    # Bulk of cases
    n = abs(n)  # weird rounding happens if n is not positive
    result = 0

    while n > 0:
        current_digit = n % 10

        if current_digit % m == 0:
            result += 1

        # cut last digit off
        n = n // 10

    return result


def is_relatively_prime(n, m):
    """
    Returns true if the only common factors of inputs n and m is 1, false
    if there are any other common factors.
    """
    return False


def travel(directions, x, y):
    """
    Takes a string of directions in the form of n, e, s, w, with any case,
    and starting coordinates x and y, and returns the new coordinates in the
    form (x_new, y_new).
    """
    result = [x, y]

    return result


def swip_swap(source, c1, c2):
    """
    Takes a source string and 2 characters c1 and c2, and returns a string
    with all instances of c1 into c2 and c2 into c1.
    """
    result = source

    return result


def compress(source):
    """
    Takes a source string and returns a string with each character followed
    by its count instead of the duplicate characters.
    """
    result = source

    return result


def longest_line_length(file_name):
    """
    Takes a file name and returns the length of the longest line in the file.
    """
    length = 0

    return length


def longest_word(file_name):
    """
    Takes a file name and returns the longest word in the with which line it
    appears on.
    """
    word = ''
    line = 1

    return str(line) + ': ' + word


def mode_digit(n):
    """
    Takes an integer n and returns the digit that appears most frequently.
    """

    return 0
