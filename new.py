
def main():
    pass

def create_values_dict(filename):
    '''
    Takes a file and creates a dictionary which contains float values for each effect in the game
    '''
    f = open(filename)
    f.readline()
    dict = {}
    for line in f:
        fields = line.split(',')
        key = fields[0].strip()
        value = float(fields[1].strip('\n').strip())
        dict[key] = value
    return dict

def create_mixing_dict(filename):
    '''
    Takes a file and creates a dictionary of dictionaries, with the following example structure:
    mixes = {
        chili: {
            'shrinking': 'refreshing',
            'athletic': 'euphoric',
            'munchies': 'toxic',
            'anti gravity': 'tropic thunder',
            'sneaky': 'bright eyed',
            'laxative': 'long faced' },
        addy: {
            'glowing': 'refreshing',
            'foggy': 'energizing',
            'sedating': 'gingeritis',
            'long faced': 'electrifying',
            'explosive': 'euphoric'}
    }

    The key in each sub-dictionary is an original effect, and the value is what the effect turns into when combined with the mixer which has the name of the sub-dictionary.
    '''

def create_mixer_dict(filename):
    '''
    Takes a file and creates a dictionary, where the key is a mixer and the value is the effect it passively adds to a drug.
    For example, 'chili' will add 'spicy'.
    mixers = {
        'chili': 'spicy',
        'viagra': 'tropic thunder'
    }
    '''

def get_effect_mult(values_dict, present_effects, effect):
    '''
    Returns the value of an effect, as long as it is not already present.
    '''

def get_total_mult(values_dict, mixer_dict, present_effects, original_effect, new_effect, mixer):
    '''
    Finds the total mult value that can be added to our drug, for the specified original effect and mixer.
    '''

main()


# print("\033[31mThis is red text\033[0m")
# print("\033[32mThis is green text\033[0m")
# print("\033[36mThis is cyan text\033[0m")
