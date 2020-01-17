import math

import hw1


def assert_equals(expected, received):
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If expected or recieved are floats,
    will do an approximate check.
    """
    # You don't need to understand how this function works
    # just look at its documentation!
    if type(expected) == 'float' or type(received) == 'float':
        match = math.isclose(expected, received)
    else:
        match = expected == received

    assert match, f'Failed: Expected {expected}, but received {received}'


def test_funky_sum():
    """
    Tests the function funky_sum
    """
    print('Testing funky_sum')

    # Notice that we have to start the function calls with "hw1." since
    # they live in another file

    # Cases from the made up "spec" for this problem
    assert_equals(1, hw1.funky_sum(1, 2, 0))
    assert_equals(2, hw1.funky_sum(1, 2, 1))
    assert_equals(1.5, hw1.funky_sum(1, 2, 0.5))
    assert_equals(1.33, hw1.funky_sum(1, 2, 0.33))

    # edge cases to test the 0 check
    assert_equals(1, hw1.funky_sum(1, 2, -1))
    assert_equals(1, hw1.funky_sum(1, 2, -0.1))
    assert_equals(1.01, hw1.funky_sum(1, 2, 0.01))

    # edge cases to test the 1 check
    assert_equals(2, hw1.funky_sum(1, 2, 2))
    assert_equals(2, hw1.funky_sum(1, 2, 2.1))
    assert_equals(1.99, hw1.funky_sum(1, 2, 0.99))


def test_count_divisible_digits():
    """
    Tests the function count_divisible_digits
    """
    print('Testing count_divisible_digits')

    # Spec tests
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(0, hw1.count_divisible_digits(24, 5))
    assert_equals(0, hw1.count_divisible_digits(1, 0))

    # Edge cases
    assert_equals(0, hw1.count_divisible_digits(42, 42))
    assert_equals(1, hw1.count_divisible_digits(0, 1))

    print('count_divisible_digits OK')


def test_is_relatively_prime():
    """
    Tests the function is_relatively_prime
    """


def test_travel():
    """
    Tests the function travel
    """


def test_swip_swap():
    """
    Tests the function swip_swap
    """
    print('Testing swip_swap')

    # Spec tests
    assert_equals('offbar', hw1.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', hw1.swip_swap('foobar', 'b', 'c'))
    assert_equals('foobar', hw1.swip_swap('foobar', 'z', 'c'))

    # Edge cases
    assert_equals('', hw1.swip_swap('', 'b', 'c'))
    assert_equals('foo ar', hw1.swip_swap('foobar', 'b', ' '))

    print('swip_swap OK')


def test_compress():
    """
    Tests the function compress
    """
    print('Testing compress')


def test_longest_line_length():
    """
    Tests the function longest_line_length
    """
    print('Testing longest_line_length')

    # Spec test
    assert_equals(13, hw1.longest_line_length('poem.txt'))

    # Edge cases
    assert_equals(None, hw1.longest_line_length('empty.txt'))
    assert_equals(11, hw1.longest_line_length('spaces.txt'))

    print('longest_line_length OK')


def test_longest_word():
    """
    Tests the function longest_word
    """
    print('Testing longest_word')

    # Spec test
    assert_equals('3: shells', hw1.longest_word('poem.txt'))

    # Edge cases
    assert_equals(None, hw1.longest_word('empty.txt'))
    assert_equals(None, hw1.longest_word('spaces.txt'))

    print('longest_word OK')


def test_mode_digit():
    """
    Tests the function mode_digit
    """


def main():
    test_funky_sum()
    # Make sure you add the calls to all of your other functions here!
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_swip_swap()
    test_longest_word()


if __name__ == '__main__':
    main()
