# Write your functions here!


def species_count(data):
    '''
    This function takes in a pandas dataframe and returns
    the number of unique names found in the 'name' column.
    '''

    return 0


def max_level(data):
    '''
    This function takes in a pandas dataframe and returns
    a tuple containing the name of the pokemon with the highest
    level and the integer level in the format:

    (name, level)
    '''
    big_boi = (None, 0)

    return big_boi


def filter_range(data, low, high):
    '''
    This function takes in a pandas dataframe data, an inclusive
    lower bound integer, and an exclusive upper bound integer, and
    returns a list of pokemon names that have the level within those
    boundaries.
    '''
    result = list()

    return result


def mean_attack_for_type(data, type):
    '''
    This function takes in a pandas dataframe data and string type
    and returns the mean attack for the pokemon that are that type.
    '''
    mean_attack = None

    return mean_attack


def count_types(data):
    '''
    This function takes in a pandas dataframe data and returns a dictionary
    with the keys being types and the value being the number of pokemon in data
    with that type.
    '''
    counts = dict()

    return counts


def highest_stage_per_type(data):
    '''
    This function takes in a pandas dataframe data and returns a dictionary
    with the keys being types and the values being the highest value of stage
    for that type.
    '''
    highest_stage = dict()

    return highest_stage


def mean_attack_per_type(data):
    '''
    This function takes in a pandas dataframe data and returns a dictionary
    with the keys being types and the values being the average attack for that
    type.
    '''
    mean_attack = dict()

    return mean_attack
