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

    # The bulk of cases
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
    # 1 is a trivial factor, so we will not think about it
    n_factors = [i for i in range(2, n + 1) if n % i == 0]
    m_factors = [i for i in range(2, m + 1) if m % i == 0]

    # Start with assumption they are relatively prime
    result = True
    for factor in n_factors:
        if factor in m_factors:
            # They have a non-trivial common factor
            result = False

    return result


def travel(directions, x, y):
    """
    Takes a string of directions in the form of n, e, s, w, with any case,
    and starting coordinates x and y, and returns the new coordinates in the
    form (x_new, y_new).
    """
    directions = directions.lower()
    for dir in directions:
        if dir == 'n':
            y += 1
        elif dir == 's':
            y -= 1
        elif dir == 'e':
            x += 1
        elif dir == 'w':
            x -= 1

        # not a valid direction, ignore

    return '(' + str(x) + ', ' + str(y) + ')'


def swip_swap(source, c1, c2):
    """
    Takes a source string and 2 characters c1 and c2, and returns a string
    with all instances of c1 into c2 and c2 into c1.
    """
    result = ""

    for char in source:
        if char == c1:
            result += c2
        elif char == c2:
            result += c1
        else:
            result += char

    return result


def compress(source):
    """
    Takes a source string and returns a string with each character followed
    by its count instead of the duplicate characters.
    """
    result = ''
    current_char = None
    tally = 1

    for char in source:
        if current_char is None:
            # Starting case
            current_char = char
        elif current_char != char:
            # Add the last character and tally
            result += current_char + str(tally)
            # Reset
            current_char = char
            tally = 1
        else:
            # the current character for compression is shown again
            tally += 1

    # Add the last character and tally if they exist
    if current_char is not None:
        result += current_char + str(tally)

    return result


def longest_line_length(file_name):
    """
    Takes a file name and returns the length of the longest line in the file.
    """
    longest_line = None

    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            if line is not None and \
                    (longest_line is None) or (len(line) > longest_line):

                longest_line = len(line)
    return longest_line


def longest_word(file_name):
    """
    Takes a file name and returns the longest word in the with which line it
    appears on.
    """
    line_num = 0
    longest_num = 0
    longest_word = None

    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            # Track current line number
            line_num += 1
            words = line.split()
            for word in words:
                # Check that we can compare length
                if (word is not None) and \
                        ((longest_word is None) or
                            (len(word) > len(longest_word))):
                    longest_word = word
                    longest_num = line_num

    if longest_word is None:
        # File was empty
        return None

    return str(longest_num) + ': ' + longest_word


def mode_digit(n):
    """
    Takes an integer n and returns the digit that appears most frequently.
    """
    # Edge case for n = 0
    if n == 0:
        return 0  # First if statement

    n = abs(n)
    tally = [0] * 10  # Super nifty notation!

    while n > 0:
        digit = n % 10
        tally[digit] += 1
        n = n // 10  # cut off last digit

    mode = -1
    max_count = 0

    for digit in range(10):
        if max_count < tally[digit] or \
                (max_count <= tally[digit] and digit > mode):  # Second if
            max_count = tally[digit]
            mode = digit

    return mode
