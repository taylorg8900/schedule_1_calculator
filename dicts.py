

def create_values_dict(filename, key_index, value_index):
    '''
    Takes a file and creates a dictionary which contains float values for each of the 34 effects in the game
    '''
    f = open(filename)
    f.readline()
    dict = {}
    for line in f:
        fields = line.split(',')
        key = fields[key_index].strip()
        value = round(float(fields[value_index].strip().strip('\n')), 2)
        dict[key] = value
    f.close()
    return dict

def create_modify_dict(filename, dict_index, key_index, value_index):
    '''
    Takes a file and creates a dictionary of dictionaries.
    Each value in the subdictionary is what the key turns into, when the dictionary name modifies the key.

    chili + shrinking -> refreshing

    mixes = {
        chili: {
            'shrinking': 'refreshing',
            'athletic': 'euphoric',
            }
        addy: {
            'glowing': 'refreshing',
            'foggy': 'energizing',
            }
    }
    '''
    f = open(filename)
    f.readline()
    dict = {}
    for line in f:
        fields = line.split(',')
        og_effect = fields[key_index].strip()
        new_effect = fields[value_index].strip()
        mixer = fields[dict_index].strip().strip('\n')
        if mixer not in dict:
            dict[mixer] = {}
        dict[mixer][og_effect] = new_effect
    f.close()
    return dict

def create_mixer_dict(filename, key_index, value_index):
    '''
    Takes a file and creates a dictionary, where the key is a mixer and the value is the effect it passively adds to a drug.
    For example, 'chili' will add 'spicy'.
    mixers = {
        'chili': 'spicy',
        'viagra': 'tropic thunder',
        'horse semen': 'long faced'
    }
    '''
    f = open(filename)
    f.readline()
    dict = {}
    for line in f:
        fields = line.split(',')
        mixer = fields[key_index].strip()
        effect = fields[value_index].strip().strip('\n')
        dict[mixer] = effect
    f.close()
    return dict