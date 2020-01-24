# Write your solutions here!


def species_count(data):
    '''
    This function takes in a list of dicitionaries and returns
    the number of unique names found in the 'name' column.
    '''
    unique_names = set()
    count = 0

    for pokemon in data:
        name = pokemon['name']

        if name not in unique_names:
            # Unique name found
            count += 1
            unique_names.add(name)

    return count


def max_level(data):
    '''
    This function takes in a list of dictionaries and returns
    a tuple containing the name of the pokemon with the highest
    level and the integer level in the format:

    (name, level)
    '''
    max_name = None
    max_level = None

    for pokemon in data:
        # Grab relevant information
        current_level = pokemon['level']
        current_name = pokemon['name']
        # First pokemon
        if max_level is None and current_level is not None:
            max_name = current_name
            max_level = current_level

        if max_level < current_level:
            max_name = current_name
            max_level = current_level

    return (max_name, max_level)


def filter_range(data, low, high):
    '''
    This function takes in a list of dictionaries data, an inclusive
    lower bound integer, and an exclusive upper bound integer, and
    returns a list of pokemon names that have the level within those
    boundaries.
    '''
    result = list()

    for pokemon in data:
        if (pokemon['level'] >= low) and (pokemon['level'] < high):
            # Add the name to the list
            result.append(pokemon['name'])

    return result


def mean_attack_for_type(data, p_type):
    '''
    This function takes in a list of dictionaries data and string type
    and returns the mean attack for the pokemon that are that type.
    '''
    mean_attack = None
    attack_vals = list()

    for pokemon in data:
        current_type = pokemon['type']

        if p_type == current_type:
            attack_vals.append(pokemon['atk'])

    if attack_vals != list():
        # not empty
        mean_attack = sum(attack_vals) / len(attack_vals)

    return mean_attack


def count_types(data):
    '''
    This function takes in a list of dictionaries data and returns a dictionary
    with the keys being types and the value being the number of pokemon in data
    with that type.
    '''
    counts = dict()

    for pokemon in data:
        current_type = pokemon['type']

        if current_type in counts.keys():
            # Add to count
            counts[current_type] += 1
        else:
            # Add the new to type to the dictionary
            counts[current_type] = 1

    return counts


def highest_stage_per_type(data):
    '''
    This function takes in a list of dictionaries data and returns a dictionary
    with the keys being types and the values being the highest value of stage
    for that type.
    '''
    highest_stage = dict()

    for pokemon in data:
        current_type = pokemon['type']
        current_stage = pokemon['stage']

        # First condition being false guarantees that second condition can
        # be tested!
        if (current_type not in highest_stage.keys()) or \
           (current_stage > highest_stage[current_type]):

            # Higher, or didn't previously exist
            highest_stage[current_type] = current_stage

    return highest_stage


def mean_attack_per_type(data):
    '''
    This function takes in a list of dictionaries data and returns a dictionary
    with the keys being types and the values being the average attack for that
    type.
    '''
    mean_attack = dict()

    for pokemon in data:
        current_type = pokemon['type']
        current_attack = pokemon['atk']

        if current_type in mean_attack.keys():
            # append this attack to the list
            mean_attack[current_type].append(current_attack)
        else:
            # This type doesn't exist yet, create new list
            mean_attack[current_type] = [current_attack]

    for p_type in mean_attack.keys():
        # Convert each list into a mean
        attack_list = mean_attack[p_type]
        mean_attack[p_type] = sum(attack_list) / len(attack_list)

    return mean_attack
