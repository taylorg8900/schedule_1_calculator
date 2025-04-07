

def create_values_dict(filename):
    '''
    Takes a file and creates a dictionary which contains float values for each of the 34 effects in the game
    '''
    f = open(filename)
    f.readline()
    dict = {}
    for line in f:
        fields = line.split(',')
        key = fields[0].strip()
        value = round(float(fields[1].strip().strip('\n')), 2)
        dict[key] = value
    f.close()
    return dict

def create_mixing_dict(filename):
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
        og_effect = fields[0].strip()
        new_effect = fields[1].strip()
        mixer = fields[2].strip().strip('\n')
        if mixer not in dict:
            dict[mixer] = {}
        dict[mixer][og_effect] = new_effect
    f.close()
    return dict

def create_mixer_dict(filename):
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
        mixer = fields[0].strip()
        effect = fields[1].strip().strip('\n')
        dict[mixer] = effect
    f.close()
    return dict