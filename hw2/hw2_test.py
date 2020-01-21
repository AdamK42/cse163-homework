import pandas as pd

# Don't worry about this import syntax, we will talk about it later
# You can call the method using
#    assert_equals(expected, received)
#    parse(file)
from cse163_utils import assert_equals, parse

import hw2_manual
import hw2_pandas

# This file is left blank for you to fill in with your tests!


def test_manual_species_count():
    '''
    Tests the manual species_count function
    '''

    test_data = parse('pokemon_test.csv')
    print('Testing species_count')

    # Spec test
    assert_equals(3, hw2_manual.species_count(test_data))


def test_manual_max_level():
    '''
    Test the manual max_level function
    '''

    test_data = parse('pokemon_test.csv')
    print('Testing max_level')

    # Spec test
    assert_equals(('Lapras', 72), hw2_manual.max_level(test_data))


def test_manual_filter_range():
    '''
    Tests the manual filter_range function
    '''

    test_data = parse('pokemon_test.csv')
    print('Testing filter_range')

    # Spec test
    expected = ['Arcanine', 'Arcanine', 'Starmie']
    received = hw2_manual.filer_range(test_data, 30, 70)
    assert_equals(expected, received)


def test_manual_mean_attack_for_type():
    '''
    Tests the manual mean_attack_for_type function
    '''

    test_data = parse('pokemon_test.csv')
    print('Testing mean_attack_for_type')

    # Spec test
    assert_equals(47.5, hw2_manual.mean_attack_for_type(test_data, 'fire'))


def test_manual_count_types():
    '''
    Tests the manual count_types function
    '''

    test_data = parse('pokemon_test.csv')
    print('Testing count_types function')

    # Spec test
    expected = {'water': 2, 'fire': 2}
    received = hw2_manual.count_types(test_data)
    assert_equals(expected, received)


def test_manual_highest_stage_per_type():
    '''
    Tests the manual highest_stage_per_type function
    '''

    test_data = parse('pokemon_test.csv')
    print('Testing highest_stage_per_type function')

    # Spec test
    expected = {'water': 2, 'fire': 2}
    received = hw2_manual.highest_stage_per_type(test_data)
    assert_equals(expected, received)


def test_manual_mean_attack_per_type():
    '''
    Tests the manual mean_attack_per_type function
    '''

    test_data = parse('pokemon_test.csv')
    print('Testing mean_attack_per_type')

    # Spec test
    expected = {'water': 140.5, 'fire': 47.5}
    received = hw2_manual.mean_attack_per_type(test_data)
    assert_equals(expected, received)


def test_manual():
    '''
    This function groups all the manual implementation functions.
    '''

    print('Testing manual implementations.')
    # Tests
    
    # test_manual_species_count()
    # test_manual_max_level()
    # test_manual_filter_range()
    # test_manual_mean_attack_for_type()
    # test_manual_count_types()
    # test_manual_highest_stage_per_type()
    # test_manual_mean_attack_per_type()


def test_pandas():
    '''
    This function groups all the pandas implementation functions.
    '''

    print('Testing pandas implementations.')
    # Tests


def main():
    test_manual()
    test_pandas()


if __name__ == '__main__':
    main()
