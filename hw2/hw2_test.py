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
    box_data = parse('pokemon_box.csv')
    print('Testing species_count')

    # Spec test
    assert_equals(3, hw2_manual.species_count(test_data))

    # My test
    # This took a while...
    assert_equals(82, hw2_manual.species_count(box_data))


def test_manual_max_level():
    '''
    Test the manual max_level function
    '''

    test_data = parse('pokemon_test.csv')
    box_data = parse('pokemon_box.csv')
    print('Testing max_level')

    # Spec test
    assert_equals(('Lapras', 72), hw2_manual.max_level(test_data))

    # My test
    assert_equals(('Victreebel', 100), hw2_manual.max_level(box_data))


def test_manual_filter_range():
    '''
    Tests the manual filter_range function
    '''

    test_data = parse('pokemon_test.csv')
    print('Testing filter_range')

    # Spec test
    expected = ['Arcanine', 'Arcanine', 'Starmie']
    received = hw2_manual.filter_range(test_data, 30, 70)

    assert_equals(expected, received)

    # My test
    expected = []
    received = hw2_manual.filter_range(test_data, 36, 67)

    assert_equals(expected, received)


def test_manual_mean_attack_for_type():
    '''
    Tests the manual mean_attack_for_type function
    '''

    test_data = parse('pokemon_test.csv')
    print('Testing mean_attack_for_type')

    # Spec test
    assert_equals(47.5, hw2_manual.mean_attack_for_type(test_data, 'fire'))

    # My test
    assert_equals(None, hw2_manual.mean_attack_for_type(test_data, 'fairy'))


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

    # My test
    my_data = parse('my_pokemon.csv')

    expected = {'water': 2, 'fire': 2, 'pyschic': 1, 'normal': 1}
    received = hw2_manual.count_types(my_data)

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

    # My test
    my_data = parse('my_pokemon.csv')

    expected = {'water': 2, 'fire': 2, 'pyschic': 2, 'normal': 0}
    received = hw2_manual.highest_stage_per_type(my_data)

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

    # My test
    my_data = parse('my_pokemon.csv')

    expected = {'water': 140.5, 'fire': 47.5, 'pyschic': 40, 'normal': 0}
    received = hw2_manual.mean_attack_per_type(my_data)

    assert_equals(expected, received)


def test_pandas_species_count():
    '''
    Tests the pandas species_count function
    '''

    test_data = pd.read_csv('pokemon_test.csv')
    print('Testing species_count')

    # Spec test
    assert_equals(3, hw2_pandas.species_count(test_data))


def test_pandas_max_level():
    '''
    Test the pandas max_level function
    '''

    test_data = pd.read_csv('pokemon_test.csv')
    print('Testing max_level')

    # Spec test
    assert_equals(('Lapras', 72), hw2_pandas.max_level(test_data))


def test_pandas_filter_range():
    '''
    Tests the pandas filter_range function
    '''

    test_data = pd.read_csv('pokemon_test.csv')
    print('Testing filter_range')

    # Spec test
    expected = ['Arcanine', 'Arcanine', 'Starmie']
    received = hw2_pandas.filer_range(test_data, 30, 70)
    assert_equals(expected, received)


def test_pandas_mean_attack_for_type():
    '''
    Tests the pandas mean_attack_for_type function
    '''

    test_data = pd.read_csv('pokemon_test.csv')
    print('Testing mean_attack_for_type')

    # Spec test
    assert_equals(47.5, hw2_pandas.mean_attack_for_type(test_data, 'fire'))


def test_pandas_count_types():
    '''
    Tests the pandas count_types function
    '''

    test_data = pd.read_csv('pokemon_test.csv')
    print('Testing count_types function')

    # Spec test
    expected = {'water': 2, 'fire': 2}
    received = hw2_pandas.count_types(test_data)
    assert_equals(expected, received)


def test_pandas_highest_stage_per_type():
    '''
    Tests the pandas highest_stage_per_type function
    '''

    test_data = pd.read_csv('pokemon_test.csv')
    print('Testing highest_stage_per_type function')

    # Spec test
    expected = {'water': 2, 'fire': 2}
    received = hw2_pandas.highest_stage_per_type(test_data)
    assert_equals(expected, received)


def test_pandas_mean_attack_per_type():
    '''
    Tests the pandas mean_attack_per_type function
    '''

    test_data = pd.read_csv('pokemon_test.csv')
    print('Testing mean_attack_per_type')

    # Spec test
    expected = {'water': 140.5, 'fire': 47.5}
    received = hw2_pandas.mean_attack_per_type(test_data)
    assert_equals(expected, received)


def main():
    '''
    This function runs all the tests in the file.
    '''

    print('Testing manual implementations.')

    test_manual_species_count()
    test_manual_max_level()
    test_manual_filter_range()
    test_manual_mean_attack_for_type()
    test_manual_count_types()
    test_manual_highest_stage_per_type()
    test_manual_mean_attack_per_type()

    print('Testing pandas implementations.')

    # test_pandas_species_count()
    # test_pandas_max_level()
    # test_pandas_filter_range()
    # test_pandas_mean_attack_for_type()
    # test_pandas_count_types()
    # test_pandas_highest_stage_per_type()
    # test_pandas_mean_attack_per_type()


if __name__ == '__main__':
    main()
