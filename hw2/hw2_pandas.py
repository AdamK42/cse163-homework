# Name: Adam Klingler
# Section: AB
# Description: This program contains functions for manipulating pokemon data
# in various ways using pandas dataframe and series features.

# Write your functions here!
import math


def species_count(data):
    '''
    This function takes in a pandas dataframe and returns
    the number of unique names found in the 'name' column.
    '''

    return len(data['name'].unique())


def max_level(data):
    '''
    This function takes in a pandas dataframe and returns
    a tuple containing the name of the pokemon with the highest
    level and the integer level in the format:

    (name, level)
    '''
    # Find the index of the highest level
    max_index = data['level'].idxmax()

    max_name = data.loc[max_index, 'name']
    max_level = data.loc[max_index, 'level']
    return (max_name, max_level)


def filter_range(data, low, high):
    '''
    This function takes in a pandas dataframe data, an inclusive
    lower bound integer, and an exclusive upper bound integer, and
    returns a list of pokemon names that have the level within those
    boundaries.
    '''
    # masking
    is_between = (data['level'] >= low) & (data['level'] < high)

    panda_names = data[is_between]['name']

    # panda_names is still a series, need python lists
    return list(panda_names)


def mean_attack_for_type(data, p_type):
    '''
    This function takes in a pandas dataframe data and a pokemon type
    and returns the mean attack for the pokemon that are that type.
    '''
    # Mask the types
    is_type = data['type'] == p_type

    mean_attack = data[is_type]['atk'].mean()

    # Check for NaN
    if math.isnan(mean_attack):
        # No attack, return None as per spec
        return None
    else:
        # Valid value, return mean
        return mean_attack


def count_types(data):
    '''
    This function takes in a pandas dataframe data and returns a dictionary
    with the keys being types and the value being the number of pokemon in data
    with that type.
    '''
    # We want to count the number of pokemon per type
    # I am using names because I know strings will behave how I want
    counts = data.groupby('type')['name'].count()

    # Counts is a series, want a dictionary
    return dict(counts)


def highest_stage_per_type(data):
    '''
    This function takes in a pandas dataframe data and returns a dictionary
    with the keys being types and the values being the highest value of stage
    for that type.
    '''
    # We want max stage per type
    highest_stage = data.groupby('type')['stage'].max()

    # highest_stage is a series, want a dictionary
    return dict(highest_stage)


def mean_attack_per_type(data):
    '''
    This function takes in a pandas dataframe data and returns a dictionary
    with the keys being types and the values being the average attack for that
    type.
    '''
    # We want mean attack per type
    mean_attack = data.groupby('type')['atk'].mean()

    # mean_attack is a series, want a dictionary
    return dict(mean_attack)
